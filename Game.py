from Board import Board
from Card import Card
from Player import Player

import tkinter as tk
from PIL import Image, ImageTk
import random

import sys
sys.setrecursionlimit(20000)

def create_deck(gui):
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
    cards = dict(zip(names,moves))
    deck = []
    for card in cards.keys():
        if gui:
            deck.append(Card(card, cards[card], load_image(card)))
        else:
            deck.append(Card(card, cards[card], None))
    return deck

def load_image(card):
    img = Image.open("res/" + card +".png")
    h = int(img.height//1.5)
    w = int(img.width//1.5)
    img = img.resize((w,h), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(img)
    return img

#JacobsNotes - look up Named Tuples

class Game:
    def __init__(self, p1, p2, gui=False):
        self.gui = gui
        self.deck = create_deck(gui)
        self.players = [Player(p1), Player(p2)]
        self.deal_hands()  # creates self.mid_card
        self.board = Board()
        self.current = 0
        self.turns = 0
        
        self.main_loop()


    def deal_hands(self):
        """
        Gets 5 random cards from the deck and deals 2 to each player.
        The remaining card is the middle card.
        """
        cards = random.sample(self.deck, 5)
        # cards = [self.deck[6] for i in range(5)]

        for p in self.players:
            p.hand = cards[0:2]
            cards = cards[2:]
        self.mid_card = cards[0]

    def take_move(self, card, start, end):  # Change to start, action as it's easy to calculate end?
        """
        Processes a legal move and changes the current player.
        Start and End are tuple co-ordinates of the move.
        """
        self.turns += 1
        self.board.move_piece(start, end)

        if self.players[self.current].hand[0].name == card.name:
            self.players[self.current].hand[0], self.mid_card = self.mid_card, self.players[self.current].hand[0]

        elif self.players[self.current].hand[1].name == card.name:
            self.players[self.current].hand[1], self.mid_card = self.mid_card, self.players[self.current].hand[1]

        self.current = 1 - self.current

    def main_loop(self):
        """
        Prompts the current player to take a turn until the game ends.
        """
        while True:
            self.board.print_board()

            card, start, end = self.players[self.current].get_move(self)
            if card.name in [self.players[self.current].hand[0].name, self.players[self.current].hand[1].name]:
                self.take_move(card, start, end)
            if self.board.is_won():
                self.board.print_board()
                print()
                print("Player " + str(1 - self.current + 1) + " won!")
                break

    def reset(self):
        self.deal_hands()  # creates self.mid_card
        self.board.reset()
        self.current = 0
        self.turns = 0

class GUIGame(Game):
    def __init__(self, p1, p2, root, battles=False):
        # self.root = tk.Tk()
        self.root = root
        self.gui_cards = []
        super().__init__(p1, p2, True)

        self.battles = battles #False or integer

        self.create_board()
        self.create_titlescore()
        self.root.mainloop()

    def main_loop(self):
        #This is intentional, Tkinter handles its own main loop
        pass

    def on_click(self, i, j, event):

        type_of_piece = event.widget.config()['text'][4]
        position = event.widget.myId
        print("Clicked on " + type_of_piece + " at position " + str(position))

        if not self.players[self.current].strategy is None:

            if self.turns > 100:
                print("Draw!")
                self.reset()
            if not self.board.is_won():
                card, start, end = self.players[self.current].get_move(self)
                self.take_move(card, start, end)
            else:
                self.battles -= 1
                #self.board.print_board()
                print()
                print("Player " + str(1 - self.current + 1) + " won!")
                self.players[1-self.current].score += 1
                self.update_titlescore()
                self.reset()

            self.update_board()
            self.update_hands()

            if self.battles > 0:
                self.root.update()
                self.on_click(i, j, event)


    def create_titlescore(self):
        self.score0 = tk.Label(self.root,text=0, font=("Helvetica", 64))
        self.score0.grid(row=2,column=0)
        self.score1 = tk.Label(self.root,text=0, font=("Helvetica", 64))
        self.score1.grid(row=2,column=2)

    def update_titlescore(self):
        self.score0['text'] = self.players[0].score
        self.score1['text'] = self.players[1].score

    def create_board(self):
        self.gui_board = tk.Frame(self.root)
        self.gui_board.grid(row=1,column=1)  

        self.gui_labelgrid = [ [None]*5 for _ in range(5) ]

        for i,row in enumerate(self.board.board_state):
            for j,col in enumerate(row):
                text = "   "
                colour = "brown"
                relief = "sunken"

                if col:
                    text = " S "
                    if col.master:
                        text = " M "
                    colour = {0:"red", 1:"blue"}[col.player]
                    relief = "raised"
                #colour, kind = col.player
                #text = {"maser":, "student":' S ', '':'}[kind]
                #text = {"master":'', "student":'', '': '}[kind]

                L = tk.Label(self.gui_board, text=text, bg=colour, font=('Courier', 32), borderwidth=4, relief=relief)
                L.grid(row=i,column=j)
                L.myId = (i,j)
                L.bind('<Button-1>',lambda e,i=i,j=j: self.on_click(i,j,e))
                self.gui_labelgrid[i][j] = L

    def update_board(self):
        for i, row in enumerate(self.board.board_state):
            for j,col in enumerate(row):
                text = "   "
                colour = "brown"
                relief = "sunken"

                if col:
                    text = " S "
                    if col.master:
                        text = " M "
                    colour = {0:"red", 1:"blue"}[col.player]
                    relief = "raised"

                self.gui_labelgrid[i][j]['text'] = text
                self.gui_labelgrid[i][j]['relief'] = relief
                self.gui_labelgrid[i][j]['bg'] = colour

    def deal_hands(self):
        super().deal_hands()

        #Create player 1 and player 2 hands
        for i, j in enumerate([0,2]):
            frame = tk.Frame(self.root)
            frame.grid(row=1, column=j)
            self.deal_hand(frame, self.players[i].hand, i+1, self.players[i].strategy.__class__.__name__)

        #Create the mid card
        frame = tk.Frame(self.root)
        frame.grid(row=2, column=1)
        self.deal_hand(frame, [self.mid_card])


    def deal_hand(self, frame, hand, player=None, player_name=None):
        if player:
            title = tk.Label(frame,text="Player " + str(player) + " hand ("+ str(player_name) + ")")
        else:
            title = tk.Label(frame, text="Middle Card")
        title.grid(row=0,column=0)

        for i, card in enumerate(hand):
            panel = tk.Button(frame, image = card.image)
            panel.grid(row=i+1,column=0)
            panel.bind('<Button-1>', lambda e, i=i: self.on_card_click(i, hand, e))
            self.gui_cards.append(panel)

    def on_card_click(self, i, hand, event):
        print(hand[i].name)



    def update_hands(self):
        cards = []
        for p in self.players:
            cards += p.hand
        cards.append(self.mid_card)
        for i in range(len(cards)):
            self.gui_cards[i]['image'] = cards[i].image
