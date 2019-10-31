from Board import Board
from Card import Card
from Player import Player
from Robots.AssassinAndy import AssassinAndy
from Robots.DirectDerek import DirectDerek
from Robots.ErraticErin import ErraticErin
from Robots.RandomRebecca import RandomRebecca
from Robots.FirstFinley import First_Finley

import tkinter as tk
from PIL import ImageTk, Image


def create_deck():
    names = "tiger dragon frog rabbit crab elephant goose rooster monkey mantis horse ox crane boar eel cobra".split()
    moves = [
        [(-2, 0), (1, 0)],
        [(-1, -2), (-1, 2), (1, -1), (1, 1)],
        [(-1, -1), (0, -2), (1, 1)],
        [(-1, 1), (0, 2), (1, -1)],
        [(-1, 0), (0, -2), (0, 2)],
        [(-1, -1), (-1, 1), (0, -1), (0, 1)],
        [(-1, -1), (0, -1), (0, 1), (1, 1)],
        [(-1, 1), (0, -1), (0, 1), (1, -1)],
        [(-1, -1), (-1, 1), (1, -1), (1, 1)],
        [(-1, -1), (-1, 1), (1, 0)],
        [(-1, 0), (0, -1), (1, 0)],
        [(-1, 0), (0, 1), (1, 0)],
        [(-1, 0), (1, -1), (1, 1)],
        [(-1, 0), (0, -1), (0, 1)],
        [(-1, -1), (0, 1), (1, -1)],
        [(-1, 1), (0, -1), (1, 1)]
        ]
    
    cards = {x:y for x in names for y in moves}
    deck = []

    for card in cards.keys():
        deck.append(Card(card, cards[card], load_image(card)))

    return deck

    return [
    Card("tiger", [(-2, 0), (1, 0)], load_image(card)),
    Card("dragon", [(-1, -2), (-1, 2), (1, -1), (1, 1)], load_image(card)),
    Card("frog", [(-1, -1), (0, -2), (1, 1)], load_image(card)),
    Card("rabbit", [(-1, 1), (0, 2), (1, -1)], load_image(card)),
    Card("crab", [(-1, 0), (0, -2), (0, 2)], load_image(card)),
    Card("elephant", [(-1, -1), (-1, 1), (0, -1), (0, 1)], load_image(card)),
    Card("goose", [(-1, -1), (0, -1), (0, 1), (1, 1)], load_image(card)),
    Card("rooster", [(-1, 1), (0, -1), (0, 1), (1, -1)], load_image(card)),
    Card("monkey", [(-1, -1), (-1, 1), (1, -1), (1, 1)], load_image(card)),
    Card("mantis", [(-1, -1), (-1, 1), (1, 0)], load_image(card)),
    Card("horse", [(-1, 0), (0, -1), (1, 0)], load_image(card)),
    Card("ox", [(-1, 0), (0, 1), (1, 0)], load_image(card)),
    Card("crane", [(-1, 0), (1, -1), (1, 1)], load_image(card)),
    Card("boar", [(-1, 0), (0, -1), (0, 1)], load_image(card)),
    Card("eel", [(-1, -1), (0, 1), (1, -1)], load_image(card)),
    Card("cobra", [(-1, 1), (0, -1), (1, 1)], load_image(card))
    ]

def load_image(card):
    img = Image.open("res/" + card +".png")
    img = img.resize((200,200), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(img)
    return img

#JacobsNotes - look up Named Tuples

class Game:
    def __init__(self, p1, p2):
        self.deck = create_deck()
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
        self.board.move_piece(start, end)

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
                self.board.print_board()
                print()
                print("Player " + str(1 - self.current + 1) + " won!")
                break

<<<<<<< HEAD
class GUIGame(Game):
    def __init__(self, p1, p2):
        self.root = tk.Tk()
        super().__init__(p1, p2)
        
        #self.game = Game()

        self.title = tk.Label(self.root,text="Onitama!", font=("Helvetica", 64))
        self.title.grid(row=0,column=1)
        self.create_board()
        self.deal_hands()

        self.rscore = tk.Label(self.root,text=0, font=("Helvetica", 64))
        self.rscore.grid(row=2,column=0)
        self.bscore = tk.Label(self.root,text=0, font=("Helvetica", 64))
        self.bscore.grid(row=2,column=2)

        self.root.mainloop()

    def create_board(self):
        pass

    def deal_hands(self):
        super().deal_hands()

        #Create player 1 and player 2 hands
        for i, j in enumerate([0,2]):
            frame = tk.Frame(self.root)
            frame.grid(row=1, column=j)
            self.deal_hand(frame, self.players[i].hand)

        #Create the mid card
        frame = tk.Frame(self.root)
        frame.grid(row=2, column=1)
        self.deal_hand(frame, [self.mid_card])

    def deal_hand(self, frame, hand):
        title = tk.Label(frame,text="It's a hand")
        title.grid(row=0,column=0)

        for i, card in enumerate(hand):
            panel = tk.Label(frame, image = card.image)
            panel.grid(row=i+1,column=0)


    def update_board(self):
        pass

    def update_actions(self):
        pass

    def hello():
        pass

finley1 = First_Finley
finley2 = First_Finley

game = GUIGame(finley1.decide_move, finley2.decide_move)game = GUIGame(finley1.decide_move, finley2.decide_move)
=======
robot1 = AssassinAndy()
robot2 = ErraticErin()

game = Game(robot1, robot2, create_deck())
>>>>>>> 31d7f8c995f21eec4b58b729f53ecd3763ce65be
