import random

"""Simulation of the game Onitama.
For reference, the blue shrine is [0,2] and the red shrine is [4,2]"""


class Game:

    def __init__(self, board_state, cards, pieces):
        self.board_state = board_state
        self.cards = cards
        self.pieces = pieces
        self.current_player = None

    """Deals the cards and decides starting player."""

    def set_up(self):
        random.shuffle(self.cards)  # For now uses the top 5 cards of the deck.
        self.cards = self.cards[:5]
        # self.cards = random.shuffle(self.cards)[:5] To use the whole deck
        self.cards[0].holder = 'r'
        self.cards[1].holder = 'r'
        self.cards[2].holder = 'b'
        self.cards[3].holder = 'b'
        self.cards[4].holder = 'm'
        self.current_player = self.cards[4].start_player

    """Returns true if the game is in a winning state. 
    Current player is used to find out who won.
    This should be run after the current player makes a move."""

    def is_won(self):
        # There is a piece on the red shrine and it is blue
        if isinstance(self.board_state[0][2], Piece) and self.board_state[0][2].color == 'b' and self.board_state[4][
            2].type == 'master':
            return True

        # There is a piece on the blue shrine and it is red
        if isinstance(self.board_state[4][2], Piece) and self.board_state[4][2].color == 'r' and self.board_state[4][
            2].type == 'master':
            return True

        # There are less than 2 master pawns
        master_pawns_counter = 0
        for row in self.board_state:
            for square in row:
                if isinstance(square, Piece) and square.type == "master":
                    master_pawns_counter += 1
        if master_pawns_counter < 2:
            return True

        return False

    """Uses a move from a card on a piece."""

    def use_move(self, card, move_index, piece):
        if self.move_legal(card, move_index, piece):
            piece_position = self.get_piece_position(piece)
            move = card.moves[move_index]
            # inverts the move if playing from the top of the board
            if piece.color == 'b':
                # removes any piece in the space the piece is moving to
                self.remove_piece(self.board_state[piece_position[0] + move[0]][piece_position[1] + move[1]])
                # sets the new space to the piece
                self.board_state[piece_position[0] + move[0]][piece_position[1] + move[1]] = piece
            else:
                # removes any piece in the space the piece is moving to
                self.remove_piece(self.board_state[piece_position[0] - move[0]][piece_position[1] - move[1]])
                # sets where the piece was to None
                # sets the new space to the piece
                self.board_state[piece_position[0] - move[0]][piece_position[1] - move[1]] = piece
            # sets where the piece was to None
            self.board_state[piece_position[0]][piece_position[1]] = None
            # swaps the card that was used with the middle card
            self.swap_cards(card)
            return True
        else:
            return False

    """Checks to see if the current player must pass. 
    This is false if all possible moves they could take are illegal."""

    def no_moves(self):
        for card in self.cards:
            if card.holder == self.current_player:
                for move_index in range(0, len(card.moves)):
                    for piece in pieces:
                        if self.move_legal(card, move_index, piece):
                            return False
        return True

    """Checks if a move is legal. Also checks that the piece and the card are legal for the current player."""

    def move_legal(self, card, move_index, piece):
        # if holding the card, move index is valid and piece belongs to current turn player
        if card.holder == self.current_player and 0 <= move_index < len(
                card.moves) and piece.color == self.current_player:

            piece_position = self.get_piece_position(piece)
            move = card.moves[move_index]
            # calculate where the piece will go
            if piece.color == 'b':
                end_position = (piece_position[0] + move[0], piece_position[1] + move[1])
            else:
                end_position = (piece_position[0] - move[0], piece_position[1] - move[1])
            x = end_position[0]
            y = end_position[1]
            # if the x and y of the move is still in the board
            if 0 <= x < len(self.board_state[0]) and 0 <= y < len(self.board_state):
                # if the space is not a friendly piece
                if not (isinstance(self.board_state[x][y], Piece) and self.board_state[x][
                    y].color == self.current_player):
                    return True
        return False

    """Gets the position of a piece on the board"""

    def get_piece_position(self, piece):
        for i in range(0, len(self.board_state)):
            for j in range(0, len(self.board_state[i])):
                if isinstance(self.board_state[i][j], Piece) and self.board_state[i][j].id == piece.id:
                    return i, j

    """Removes a piece from the list of pieces if a piece was passed in"""

    def remove_piece(self, piece):
        pop_index = None
        if piece:
            for i in range(0, len(pieces)):
                if self.pieces[i].id == piece.id:
                    pop_index = i
            if pop_index:
                self.pieces.pop(pop_index)

    """Swaps cards with the middle"""

    def swap_cards(self, player_card):
        for card in cards:
            # if the card is in the middle
            if card.holder == 'm':
                # the current player has it now
                card.holder = self.current_player
            # if the card was just played
            if card.name == player_card.name:
                # the middle has it now
                card.holder = 'm'

    def end_turn(self):
        if self.is_won():
            return self.current_player
        if self.current_player == 'b':
            self.current_player = 'r'
        else:
            self.current_player = 'b'
        return None

    def process_input(self, t):
        if t == "1":
            for card in self.cards:
                print(str(card.name) + ": Held by " + str(card.holder))
            return None
        elif t == "2":
            print(self.print_board())
            return None
        elif t == "3":
            return True
        else:
            print("Please enter a valid command.")
            return None

    def process_move(self, name, index, piece_id):
        result = False
        for card in self.cards:
            if card.name == name:
                for piece in self.pieces:
                    if piece.id == int(piece_id):
                        result = self.use_move(card, int(index), piece)
                        if not result:
                            print("Invalid move")
                        return result
        print("Check your input is correct")
        return result

    def process_swap(self, name):
        for card in self.cards:
            if card.name == name and self.current_player == card.holder:
                self.swap_cards(card)
                return True
        print("Bad name. Lowercase string input of a card name you are holding.")
        self.process_input("cards")
        return False

    def print_board(self):
        for row in self.board_state:
            row_string = ""
            for space in row:
                if isinstance(space, Piece):
                    row_string += (str(space.color) + str(space.id))
                else:
                    row_string += ("##")
            print(row_string)


class Card:

    def __init__(self, name, moves, start_player, holder):
        self.name = name
        self.moves = moves
        self.start_player = start_player
        self.holder = holder


class Piece:

    def __init__(self, id, type, color):
        self.id = id
        self.type = type
        self.color = color


def main():
    game = Game(default_board, cards, pieces)
    game.set_up()
    print("Welcome to Onikawa! This is a 2 player game similar to chess.\n")
    print("Starting player is " + game.current_player)
    while not game.is_won():
        print("Next turn: " + game.current_player)
        if game.no_moves():
            swap_done = False
            while not swap_done:
                print("You have no possible moves.")
                swap = input("Enter the name of the card you want to swap with the middle: ")
                swap_done = game.process_swap(swap)
        else:
            print("\nCommands:\n"
                  "1: prints a list of the cards and who owns them\n"
                  "2: prints the board\n"
                  "3: enters the make a move menu\n")
            action = False
            while not action:
                t = input("Enter a command: ")
                action = game.process_input(t)
            move = False
            while not move:
                name = input("Enter the card name: ")
                index = input("Enter the move index: ")
                piece_id = input("Enter the piece id: ")
                move = game.process_move(name, index, piece_id)
        game.end_turn()
    print("The winner is " + game.current_player)


pieces = [
    Piece(0, 'student', 'r'),
    Piece(1, 'student', 'r'),
    Piece(2, 'student', 'r'),
    Piece(3, 'student', 'r'),
    Piece(4, 'master', 'r'),
    Piece(5, 'student', 'b'),
    Piece(6, 'student', 'b'),
    Piece(7, 'student', 'b'),
    Piece(8, 'student', 'b'),
    Piece(9, 'master', 'b')
]

cards = [
    Card("tiger", [(-2, 0), (1, 0)], 'b', None),
    Card("dragon", [(-1, -2), (-1, 2), (1, -1), (1, 1)], 'r', None),
    Card("frog", [(-1, -1), (0, -2), (1, 1)], 'r', None),
    Card("rabbit", [(-1, 1), (0, -2), (1, -1)], 'r', None),
    Card("crab", [(-1, 0), (0, -2), (0, 2)], 'b', None),
    Card("elephant", [(-1, -1), (-1, 1), (0, -1), (0, 1)], 'r', None),
    Card("goose", [(-1, -1), (0, -1), (0, 1), (1, 1)], 'b', None),
    Card("rooster", [(-1, 1), (0, -1), (0, 1), (1, -1)], 'r', None),
    Card("monkey", [(-1, -1), (-1, 1), (1, -1), (1, 1)], 'b', None),
    Card("mantis", [(-1, -1), (-1, 1), (1, 0)], 'r', None),
    Card("horse", [(-1, 0), (0, -1), (1, 0)], 'r', None),
    Card("ox", [(-1, 0), (0, 1), (1, 0)], 'b', None),
    Card("crane", [(-1, 0), (1, -1), (1, 1)], 'b', None),
    Card("boar", [(-1, 0), (0, -1), (0, 1)], 'r', None),
    Card("eel", [(-1, -1), (0, 1), (1, -1)], 'b', None),
    Card("cobra", [(-1, 1), (0, -1), (1, 1)], 'r', None)
]

default_board = [[pieces[0], pieces[1], pieces[4], pieces[2], pieces[3]],
                 [None, None, None, None, None],
                 [None, None, None, None, None],
                 [None, None, None, None, None],
                 [pieces[5], pieces[6], pieces[9], pieces[7], pieces[8]]]

main()
