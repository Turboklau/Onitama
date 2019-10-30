class Game:
    def __init__(p1, p22, deck):
        self.deck = deck
        self.players = [Player(p1), Player(p2)]
        board = Board()
        self.current = 0

    def deal_hand(p1, p2):
        cards = random.sample(self.deck, 5)
        p1.hand = cards[0:2]
        p2.hand = cards[2:4]
        self.extra_card = cards[4]

    def take_move(card, start, end):
        self.players[current].get_move
        self.board.move_piece(card, colour, start, end)
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
