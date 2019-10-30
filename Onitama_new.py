class Game:
    def __init__():
        board = Board()

    def take_move(card, start, end):
        if self.board.possible_move(card, start, end):
            #move_piece
            #swap_card
            #
            #if board.is_won
            #   self.reset
            #
            #swap_turn

class Board:
    def __init__():
        self.extra_card = None
        create_board()

    def create_board():
        self.pieces = None
        self.board = None
        #Pieces are in board

    def is_won():
        return False

    def possible_move(card, start, end):
        return False

    def move_piece(start, end):
        if not possible_move(card, start end):
            return False
        else:
            pass #Do move
            return True


class Piece:
    def __init__(self, player, location=None, master=False):
        self.master = master
        self.player = player
        location = location


class Player:
    def __init__(self, hand=[], score=0):
        self.hand = hand
        self.score = score

class Card:
    def __init__(self, name=None, moves=None, image=None):
        self.name = name
        self.moves = moves
        self.image = image
