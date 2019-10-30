default_board = ([None, None, None, None, None],
                 [None, None, None, None, None],
                 [None, None, None, None, None],
                 [None, None, None, None, None],
                 [None, None, None, None, None])

class Game:
    def __init__(self, p1, p22, deck):
        self.deck = deck
        self.players = [Player(p1), Player(p2)]
        board = Board()
        self.current = 0
        self.mid_card = mid_card

    def deal_hand(self, p1, p2):
        cards = random.sample(self.deck, 5)
        p1.hand = cards[0:2]
        p2.hand = cards[2:4]
        self.extra_card = cards[4]

    def main_loop(self):

        while True:
            card, start, end = self.players[current].get_move(self.board, self.current, self.players)
            x = self.take_move(self, card, start, end)
            if x:
                break



    def take_move(self, card, start, end):
        #card, start, end = self.players[current].get_move(board, self.current, self.players)
        assert self.board.move_piece(card, self.current, start, end)

        if self.players[self.current].hand[0] == card:
            self.players[self.current].hand[0], self.mid_card = self.mid_card, self.players[self.current].hand[0]

        elif self.players[self.current].hand[1] == card:
            self.players[self.current].hand[1], self.mid_card = self.mid_card, self.players[self.current].hand[1]
        
        self.current = 1 - self.current

        if board.is_won:
            #self.reset
            return True
        return False

class Board:

    def __init__(self, middle_card):
        self.board_state = list(default_board)
        self.pieces = set()
        self.populate_board()

    def populate_board(self):

        for index, num in enumerate([0, 0, 0, 0, 0, -1, -1, -1, -1, -1]):

            if num == 0:
                piece = Piece(player1)
            else:
                piece = Piece(player2)

            self.pieces.add(piece)
            piece.location = self.board_state[num][index%5]
            self.board_state[num][index%5] = piece
            if index%5 == 2:
                piece.master = True

    def is_won(self):
        if isinstance(self.board_state[0][2], Piece) and self.board_state[0][2].color == player2 and self.board_state[0][2].master:
            return True

        if isinstance(self.board_state[4][2], Piece) and self.board_state[4][2].color == player1 and self.board_state[4][2].master:
            return True

        return self.master_captured()

    def master_captured(self):
        num_masters = 0
        for piece in self.pieces:
            if piece.master:
                num_masters += 1
        return num_masters < 2

    def is_possible_move(self, card, color, start, end):
        start_x, start_y = start
        end_x, end_y = end
        piece = self.board_state[start_x][start_y]
        if isinstance(piece, Piece) and self.on_board_and_not_friendly(end_x, end_y, color):
            for move in card.moves:
                if (color == player1 and end == (start_x + move[0], start_y + move[1])) \
                        or (color == player2 and end == (start_x - move[0], start_y - move[1])):
                    return True
        return False

    def on_board_and_not_friendly(self, x, y, color):
        if 0 <= x < len(self.board_state[0]) and 0 <= y < len(self.board_state):
            return not isinstance(self.board_state[x][y], Piece) and self.board_state[x][y].color == color

    def move_piece(self, card, color, start, end):
        if self.is_possible_move(card, color, start, end):
            start_x, start_y = start
            end_x, end_y = end
            self.remove_piece(end_x, end_y)
            self.board_state[end_x][end_y] = self.board_state[start_x][start_y]
            self.board_state[start_x][start_y] = None
            return True
        else:
            return False

    def remove_piece(self, end_x, end_y):
        if isinstance(self.board_state[end_x][end_y], Piece):
            for piece in self.pieces:
                if piece.location == [end_x][end_y]:
                    self.pieces.remove(piece)
                    return True
        return False

class Piece:
    def __init__(self, player, location=None, master=False):
        self.master = master
        self.player = player
        location = location

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
