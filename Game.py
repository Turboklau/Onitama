from Board import Board
from Card import Card
from Player import Player
from Robots.FirstFinley import First_Finley


def create_deck():
    return [
    Card("tiger", [(-2, 0), (1, 0)]),
    Card("dragon", [(-1, -2), (-1, 2), (1, -1), (1, 1)]),
    Card("frog", [(-1, -1), (0, -2), (1, 1)]),
    Card("rabbit", [(-1, 1), (0, 2), (1, -1)]),
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

#JacobsNotes - look up Named Tuples

class Game:
    def __init__(self, p1, p2, deck):
        self.deck = deck
        self.players = [Player(p1), Player(p2)]
        self.deal_hands()  # creates self.mid_card
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

    def take_move(self, card, start, end):  # Change to start, action as it's easy to calculate end?
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

finley1 = First_Finley
finley2 = First_Finley

game = Game(finley1.decide_move, finley2.decide_move, create_deck())