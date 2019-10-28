import random
import math
import copy

"""Simulation of the game Onitama.
For reference, the blue shrine is [0,2] and the red shrine is [4,2]"""

"""Global variable time!"""
player1 = 'red'
player2 = 'blue'
middle = 'middle'
color_code_red = '\x1b[0;31;47m'
color_code_blue = '\x1b[0;34;47m'
color_code_black = '\x1b[0;30;47m'
color_code_end = '\x1b[0m'

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

class Move:

    def __init__(self, card, move_index, piece, new_board_state):
        self.card = card
        self.move_index = move_index
        self.piece = piece
        self.points = -math.inf
        self.new_board_state = new_board_state


pieces = [
    Piece(0, 'student', player1),
    Piece(1, 'student', player1),
    Piece(2, 'student', player1),
    Piece(3, 'student', player1),
    Piece(4, 'master', player1),
    Piece(5, 'student', player2),
    Piece(6, 'student', player2),
    Piece(7, 'student', player2),
    Piece(8, 'student', player2),
    Piece(9, 'master', player2)
]

cards = [
    Card("tiger", [(-2, 0), (1, 0)], player2, None),
    Card("dragon", [(-1, -2), (-1, 2), (1, -1), (1, 1)], player1, None),
    Card("frog", [(-1, -1), (0, -2), (1, 1)], player1, None),
    Card("rabbit", [(-1, 1), (0, -2), (1, -1)], player1, None),
    Card("crab", [(-1, 0), (0, -2), (0, 2)], player2, None),
    Card("elephant", [(-1, -1), (-1, 1), (0, -1), (0, 1)], player1, None),
    Card("goose", [(-1, -1), (0, -1), (0, 1), (1, 1)], player2, None),
    Card("rooster", [(-1, 1), (0, -1), (0, 1), (1, -1)], player1, None),
    Card("monkey", [(-1, -1), (-1, 1), (1, -1), (1, 1)], player2, None),
    Card("mantis", [(-1, -1), (-1, 1), (1, 0)], player1, None),
    Card("horse", [(-1, 0), (0, -1), (1, 0)], player1, None),
    Card("ox", [(-1, 0), (0, 1), (1, 0)], player2, None),
    Card("crane", [(-1, 0), (1, -1), (1, 1)], player2, None),
    Card("boar", [(-1, 0), (0, -1), (0, 1)], player1, None),
    Card("eel", [(-1, -1), (0, 1), (1, -1)], player2, None),
    Card("cobra", [(-1, 1), (0, -1), (1, 1)], player1, None)
]

default_board = [[pieces[0], pieces[1], pieces[4], pieces[2], pieces[3]],
                 [None, None, None, None, None],
                 [None, None, None, None, None],
                 [None, None, None, None, None],
                 [pieces[5], pieces[6], pieces[9], pieces[7], pieces[8]]]

class Game:

    def __init__(self, board_state=default_board, cards=cards, pieces=pieces):
        self.board_state = board_state
        self.cards = cards
        self.pieces = pieces
        self.current_player = None
        self.master_captured = False

    """Deals the cards and decides starting player."""

    def set_up(self):
        self.cards = random.sample(self.cards, 5)
        self.cards[0].holder = player1
        self.cards[1].holder = player1
        self.cards[2].holder = player2
        self.cards[3].holder = player2
        self.cards[4].holder = middle
        self.current_player = self.cards[4].start_player

    """Returns true if the game is in a winning state. 
    Current player is used to find out who won.
    This should be run after the current player makes a move."""

    def is_won(self):
        # There is a piece on the red shrine and it is blue
        if isinstance(self.board_state[0][2], Piece) and self.board_state[0][2].color == player2 and \
                self.board_state[0][
                    2].type == 'master':
            return True

        # There is a piece on the blue shrine and it is red
        if isinstance(self.board_state[4][2], Piece) and self.board_state[4][2].color == player1 and \
                self.board_state[4][
                    2].type == 'master':
            return True

        if self.master_captured:
            return True

        return False

    """Uses a move from a card on a piece."""

    def use_move(self, card, move_index, piece):
        if self.move_legal(card, move_index, piece):
            piece_position = self.get_piece_position_on_board(self.board_state, piece)
            move = card.moves[move_index]
            if piece.color == player2:
                self.remove_piece(self.board_state[piece_position[0] + move[0]][piece_position[1] + move[1]])
                self.board_state[piece_position[0]][piece_position[1]] = None
                self.board_state[piece_position[0] + move[0]][piece_position[1] + move[1]] = piece
            else:
                self.remove_piece(self.board_state[piece_position[0] - move[0]][piece_position[1] - move[1]])
                self.board_state[piece_position[0]][piece_position[1]] = None
                self.board_state[piece_position[0] - move[0]][piece_position[1] - move[1]] = piece
            self.swap_cards(card)
            return True
        else:
            return False

    """Checks if a move is legal. Also checks that the piece and the card are legal for the current player."""

    def move_legal(self, card, move_index, piece):
        # if holding the card, move index is valid and piece belongs to current turn player
        if card.holder == self.current_player and 0 <= move_index < len(
                card.moves) and piece.color == self.current_player:

            piece_position = self.get_piece_position_on_board(self.board_state, piece)
            move = card.moves[move_index]
            if not (piece_position and move):
                return False
            # calculate where the piece will go
            if piece.color == player2:
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

    def get_piece_position_on_board(self, board, piece):
        for i in range(0, len(board)):
            for j in range(0, len(board[i])):
                if isinstance(board[i][j], Piece) and board[i][j].id == piece.id:
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
            if piece.type == 'master':
                self.master_captured = True

    """Swaps cards with the middle"""

    def swap_cards(self, player_card):
        for card in cards:
            # if the card is in the middle
            if card.holder == middle:
                # the current player has it now
                card.holder = self.current_player
            # if the card was just played
            if card.name == player_card.name:
                # the middle has it now
                card.holder = middle

    def end_turn(self):
        if self.is_won():
            return self.current_player
        if self.current_player == player2:
            self.current_player = player1
        else:
            self.current_player = player2
        return None

    def process_input(self, t):
        if t == "1":
            print()
            for card in self.cards:
                print(str(card.name) + ": Held by " + str(card.holder))
            return None
        elif t == "2":
            self.print_board(self.board_state)
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

    def print_board(self, board):
        print()
        for row in board:
            row_string = ""
            for space in row:
                if isinstance(space, Piece):
                    if space.color == 'red':
                        row_string += (color_code_red + str(space.type[0]) + str(space.id) + color_code_end)
                    if space.color == 'blue':
                        row_string += (color_code_blue + str(space.type[0]) + str(space.id) + color_code_end)
                else:
                    row_string += (color_code_black + "[]" + color_code_end)
            print(row_string)
        print()

    def move_list(self):
        moves = []
        for card in self.cards:
            if card.holder == self.current_player:
                for move_index in range(0, len(card.moves)):
                    for piece in pieces:
                        if self.move_legal(card, move_index, piece):
                            piece_position = self.get_piece_position_on_board(self.board_state, piece)
                            new_board_state = copy.deepcopy(self.board_state)
                            new_board_state[piece_position[0]][piece_position[1]] = None
                            if piece.color == player2:
                                new_board_state[piece_position[0] + card.moves[move_index][0]][piece_position[1] + card.moves[move_index][1]] = piece
                            else:
                                new_board_state[piece_position[0] - card.moves[move_index][0]][piece_position[1] - card.moves[move_index][1]] = piece
                            moves.append(Move(card, move_index, piece, new_board_state))


        return moves