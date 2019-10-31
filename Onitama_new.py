#JacobsNotes - look up Named Tuples
import random

player1 = 0
player2 = 1

color_code_red = '\x1b[0;31;47m'
color_code_blue = '\x1b[0;34;47m'
color_code_black = '\x1b[0;30;47m'
color_code_end = '\x1b[0m'

default_board = ([None, None, None, None, None],
                 [None, None, None, None, None],
                 [None, None, None, None, None],
                 [None, None, None, None, None],
                 [None, None, None, None, None])


class Game:
    def __init__(self, p1, p2, deck):
        self.deck = deck
        self.players = [Player(p1), Player(p2)]
        self.deal_hands() #creates self.mid_card
        self.board = Board()
        self.current = 0
        self.main_loop()

    def deal_hands(self):
        """
        Gets 5 random cards from the deck and deals 2 to each player.
        The remaining card is the middle card.
        """
        # cards = random.sample(self.deck, 5)
        cards = self.deck[3:8]

        for p in self.players:
            p.hand = cards[0:2]
            cards = cards[2:]
        self.mid_card = cards[0]

    def main_loop(self):
        """
        Prompts the current player to take a turn until the game ends.
        """
        while True:
            self.board.print_board()
            card, start, end = self.players[self.current].get_move(self.board, self.current, self.players)
            self.take_move(card, start, end)
            if self.board.is_won():
                print("Someone won!")
                self.board.print_board()
                break

    def take_move(self, card, start, end): #Change to start, action as it's easy to calculate end?
        """
        Processes a legal move and changes the current player.
        Start and End are tuple co-ordinates of the move.
        """
        assert self.board.move_piece(card, self.current, start, end)

        if self.players[self.current].hand[0] == card:
            self.players[self.current].hand[0], self.mid_card = self.mid_card, self.players[self.current].hand[0]

        elif self.players[self.current].hand[1] == card:
            self.players[self.current].hand[1], self.mid_card = self.mid_card, self.players[self.current].hand[1]
        
        self.current = 1 - self.current

class GUIGame(Game):
    def __init__(self, p1, p2, deck):
        print("test")
        #self.__init__(p1, p2, deck)

class Board:

    def __init__(self):
        self.board_state = list(default_board)
        self.pieces = set()
        self.populate_board()

    def populate_board(self):

        for index, num in enumerate([0, 0, 0, 0, 0, 4, 4, 4, 4, 4]):

            if num == 0:
                piece = Piece(1)
            else:
                piece = Piece(0)

            self.pieces.add(piece)
            piece.location = [num, index%5]
            self.board_state[num][index%5] = piece
            if index%5 == 2:
                piece.master = True

    def is_won(self):
        if isinstance(self.board_state[0][2], Piece) and self.board_state[0][2].player == player1 and self.board_state[0][2].master:
            return True

        if isinstance(self.board_state[4][2], Piece) and self.board_state[4][2].player == player2 and self.board_state[4][2].master:
            return True

        return self.master_captured()

    def master_captured(self):
        num_masters = 0
        for piece in self.pieces:
            if piece.master:
                num_masters += 1
        return num_masters < 2

    def is_possible_move(self, card, player, start, end):
        start_row, start_col = start
        end_row, end_col = end
        piece = self.board_state[start_row][start_col]
        if isinstance(piece, Piece) and self.on_board_and_not_friendly(end_row, end_col, player):
            for move in card.moves:
                if (piece.player == player1 and end == [start_row + move[0], start_col + move[1]]) \
                        or (piece.player == player2 and end == [start_row - move[0], start_col - move[1]]):
                    return True
        return False

    def on_board_and_not_friendly(self, row, col, player):
        if not (0 <= row < len(self.board_state[0]) and 0 <= col < len(self.board_state)):
            return False
        if isinstance(self.board_state[row][col], Piece) and self.board_state[row][col].player == player:
            return False

        return True


    def move_piece(self, card, player, start, end):
        if self.is_possible_move(card, player, start, end):
            start_row, start_col = start
            end_row, end_col = end
            self.remove_piece(end_row, end_col)
            self.board_state[start_row][start_col].location = [end_row, end_col]
            self.board_state[end_row][end_col] = self.board_state[start_row][start_col]
            self.board_state[start_row][start_col] = None
            return True
        else:
            return False

    def remove_piece(self, end_row, end_col):
        if isinstance(self.board_state[end_row][end_col], Piece):
            for piece in self.pieces:
                if piece.location == [end_row, end_col]:
                    piece.location = [-1, -1]
                    self.pieces.remove(piece)
                    return True
        return False

    def print_board(self):
        print()
        for row in self.board_state:
            row_string = ""
            for space in row:
                if isinstance(space, Piece):
                    if space.player == player1:
                        row_string += (color_code_red + "rp" + color_code_end)
                    if space.player == player2:
                        row_string += (color_code_blue + "bp" + color_code_end)
                else:
                    row_string += (color_code_black + "[]" + color_code_end)
            print(row_string)
        print()

class Piece:
    def __init__(self, player, location=None, master=False):
        self.master = master
        self.player = player
        self.location = location

        assert type(self.player) == int

class Player:
    def __init__(self, strategy, hand=[], score=0):
        self.strategy = strategy
        self.hand = hand
        self.score = score

    def get_move(self, board, player, players):
        return self.strategy(board, player, players)

class Card:
    def __init__(self, name=None, moves=None, image=None):
        self.name = name
        self.moves = moves
        self.image = image


def first_finley(board, me, players):
    """First Finley always takes the first legal move he can find"""

    #Inverts movement matrix if playing for opposing side
    mult = 1
    if me == 1:
        mult = -1

    my_hand = players[me].hand

    #For every move
    for card in my_hand:
        for move in card.moves:
            
            #For every piece of mine
            for piece in board.pieces:
                if piece.player == me:
                    
                    #Is that move possible? If so, take it
                    start = piece.location
                    end = [start[0]+ mult * move[0], 
                           start[1]+ mult * move[1]]

                    if board.is_possible_move(card, me, start, end):
                        print("Player " + str(me+1) + ": " + card.name)
                        return card, piece.location, end
    
    print("No available moves (I'm probably lying)")

def create_deck():
    return [
    Card("tiger", [(-2, 0), (1, 0)]),
    Card("dragon", [(-1, -2), (-1, 2), (1, -1), (1, 1)]),
    Card("frog", [(-1, -1), (0, -2), (1, 1)]),
    Card("rabbit", [(-1, 1), (0, -2), (1, -1)]),
    Card("crab", [(-1, 0), (0, -2), (0, 2)]),
    Card("elephant", [(-1, -1), (-1, 1), (0, -1), (0, 1)]),
    Card("goose", [(-1, -1), (0, -1), (0, 1), (1, 1)]),
    Card("rooster", [(-1, 1), (0, -1), (0, 1), (1, -1)]),
    Card("monkey", [(-1, -1), (-1, 1), (1, -1), (1, 1)]),
    Card("mantis", [(-1, -1), (-1, 1), (1, 0)]),
    Card("horse", [(-1, 0), (0, -1), (1, 0)]),
    Card("ox", [(-1, 0), (0, 1), (1, 0)]),
    Card("crane", [(-1, 0), (1, -1), (1, 1)]),
    Card("boar", [(-1, 0), (0, -1), (0, 1)]),
    Card("eel", [(-1, -1), (0, 1), (1, -1)]),
    Card("cobra", [(-1, 1), (0, -1), (1, 1)])
    ]

game = GUIGame(first_finley, first_finley, create_deck())