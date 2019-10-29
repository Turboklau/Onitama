import tkinter as tk#, Label, Button
import tkinter.ttk
from OnitamaForRobots import Game
from PIL import ImageTk, Image


class OnitamaGUI:
    def __init__(self):
        self.images = {}
        self.actions = [0,0,0,0,0]
        self.root = tk.Tk()
        self.game = Game()
        self.game.set_up()

      
        self.create_board()
        self.create_actions()

        self.count = 0


        self.root.mainloop()

    def on_click(self, i,j,event):
        #color = "red"
        #event.widget.config(bg=color)
        from Robots.RandomRebecca import RandomRebecca as robot
        bot = robot('red')
        bot2 = robot('blue')
        self.count += 1
        if self.count %2 == 1:
            robot_turn(bot, self.game)
        else:
            robot_turn(bot2, self.game)
        if self.game.is_won():
            self.reset()

        self.update_board()
        self.update_actions()

    def reset(self):
        self.game.reset()

    def terminate(self):
        self.root.destroy()

    def create_board(self):
        self.board = tk.Frame(self.root)
        self.board.grid(row=1,column=1)  
        #board = [ [None]*5 for _ in range(5) ]
        self.labelgrid = [ [None]*5 for _ in range(5) ]
        for i,row in enumerate(self.game.board_state):
            for j,col in enumerate(row):
                colour, kind = self.game.get_square(i, j)
                text = {"master":' M ', "student":' S ', '':'‎‎‎‏‏‎   ‎'}[kind]
                #text = {"master":'♕', "student":'♙', '':'‎‎‎‏‏‎ ‎'}[kind]

                L = tk.Label(self.board,text=text,bg=colour, font=('Courier', 80))
                L.grid(row=i,column=j)
                L.bind('<Button-1>',lambda e,i=i,j=j: self.on_click(i,j,e))
                self.labelgrid[i][j] = L

    def update_board(self):
        for i,row in enumerate(self.game.board_state):
            for j,col in enumerate(row):
                colour, kind = self.game.get_square(i, j)
                text = {"master":' M ', "student":' S ', '':'‎‎‎‏‏‎   ‎'}[kind]

                self.labelgrid[i][j]['text'] = text
                self.labelgrid[i][j]['bg'] = colour
    
    def load_image(self, card):
        img = Image.open("res/" + card +".png")
        img = img.resize((200,200), Image.ANTIALIAS)
        img = ImageTk.PhotoImage(img)
        self.images[card] = img


    def create_actions(self):
        self.left = tk.Frame(self.root)
        self.left.grid(row=1, column=0)
        self.right = tk.Frame(self.root)
        self.right.grid(row=1, column=2)
        self.extra = tk.Frame(self.root)
        self.extra.grid(row=2, column=1)
        P1 = tk.Label(self.left,text="Red Player Cards")
        Ex = tk.Label(self.extra,text="Extra")
        P2 = tk.Label(self.right,text="Blue Player Cards")
        P1.grid(row=0,column=0)
        Ex.grid(row=0,column=0)
        P2.grid(row=0,column=0)

        y = [0,1, 0, 0,1]
        x = [self.left, self.left, self.extra, self.right, self.right]
        for i in range(5):
            panel = tk.Label(x[i], image = None, text="h")
            panel.grid(row=y[i]+1,column=0)
            self.actions[i] = panel
        self.update_actions()

    def update_actions(self):
        inc = [0,2,3]

        for card in self.game.cards:
            if card.name not in self.images.keys():
                self.load_image(card.name)

            if card.holder == "red":
                row = 0
            elif card.holder == "blue":
                row = 2
            else:
                row = 1

            self.actions[inc[row]]["image"] = self.images[card.name]
            inc[row] += 1




def robot_turn(robot, game):
    move = robot.decide_move(game)
    if move:
        game.process_move(move.card.name, move.move_index, move.piece.id)
    else:
        for card in game.cards:
            if card.holder == robot.color:
                game.process_swap(card)
                break

    game.end_turn()
    return move.card.name

x = OnitamaGUI()

