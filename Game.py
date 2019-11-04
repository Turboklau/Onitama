from Board import Board
from Card import Card
from Player import Player

import tkinter as tk
from PIL import Image, ImageTk
import random, time

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
        self.main_loop()

    def deal_hands(self):
        """
        Gets 5 random cards from the deck and deals 2 to each player.
        The remaining card is the middle card.
        """
        cards = random.sample(self.deck, 5)
        #cards = [self.deck[0] for i in range(5)]
        #print(self.deck[0].moves)

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
            card, start, end = self.players[self.current].get_move(self.board, self.current, self.players, self.mid_card)
            if card in self.players[self.current].hand:
                self.take_move(card, start, end)
            if self.board.is_won():
                self.board.print_board()
                print()
                print("Player " + str(1 - self.current + 1) + " won!")
                break

class GUIGame(Game):
    def __init__(self, p1, p2):
        self.root = tk.Tk()
        self.gui_cards = []
        super().__init__(p1, p2, True)
        #self.game = Game()
        
        self.title = tk.Label(self.root,text="Onitama!", font=("Helvetica", 64))
        self.title.grid(row=0,column=1)

        self.create_board()
        self.root.mainloop()

    def main_loop(self):
        #This is intentional, Tkinter handles its own main loop
        pass

    def on_click(self, i, j, event):
        if not self.board.is_won():
            card, start, end = self.players[self.current].get_move(self.board, self.current, self.players, self.mid_card)
            self.take_move(card, start, end)
            self.update_board()
            self.update_hands()
        else:
            self.board.print_board()
            print()
            print("Player " + str(1 - self.current + 1) + " won!")

    def create_titlescore(self):
        self.rscore = tk.Label(self.root,text=0, font=("Helvetica", 64))
        self.rscore.grid(row=2,column=0)
        self.bscore = tk.Label(self.root,text=0, font=("Helvetica", 64))
        self.bscore.grid(row=2,column=2)

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

                L = tk.Label(self.gui_board,text=text,bg=colour, font=('Courier', 80), borderwidth=4, relief=relief)
                L.grid(row=i,column=j)
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
            self.gui_cards.append(panel)


    def update_hands(self):
        cards = []
        for p in self.players:
            cards += p.hand
        cards.append(self.mid_card)
        for i in range(len(cards)):
            self.gui_cards[i]['image'] = cards[i].image

        
