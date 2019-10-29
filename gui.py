import tkinter as tk#, Label, Button
import tkinter.ttk
from OnitamaForRobots import Game
from PIL import ImageTk, Image


class OnitamaGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.game = Game()
        self.game.set_up()
        self.title = tk.Label(self.root,text="Today is Onitama", font=('Courier', 64))
        self.title.grid(row=0,column=1)

        self.board = tk.Frame(self.root)
        self.board.grid(row=1,column=1)

        #self.actions = tk.Frame(self.root)
        #self.actions.grid(row=2,column=0)
        
        self.update_board()
        self.update_actions()



        self.root.mainloop()

    def on_click(self, i,j,event):
        #color = "red"
        #event.widget.config(bg=color)
        from Robots.ErraticErin import ErraticErin
        bot = ErraticErin(self.game, 'red')

        robot_turn(bot, self.game)
        if self.game.is_won():
            self.reset()

        self.update_board()

    def reset(self):
        print("aahhhhhh")
        self.root = tk.Tk()
        self.game = Game()
        self.game.set_up()
        self.update_board()
        self.update_actions()

    def pvp(self):
        self.pvp.destroy()



    def update_board(self):
        #board = [ [None]*5 for _ in range(5) ]
        for i,row in enumerate(self.game.board_state):
            for j,col in enumerate(row):
                colour, kind = self.game.get_square(i, j)
                text = {"master":' M ', "student":' S ', '':'‎‎‎‏‏‎   ‎'}[kind]
                #text = {"master":'♕', "student":'♙', '':'‎‎‎‏‏‎ ‎'}[kind]

                L = tk.Label(self.board,text=text,bg=colour, font=('Courier', 80))
                L.grid(row=i,column=j)
                L.bind('<Button-1>',lambda e,i=i,j=j: self.on_click(i,j,e))
                #tk.ttk.Separator(self.root, orient='vertical').grid(column=1, row=0, rowspan=5, sticky='ns')

    def update_actions(self):

        self.left = tk.Frame(self.root)
        self.left.grid(row=1, column=0)

        self.right = tk.Frame(self.root)
        self.right.grid(row=1, column=2)

        self.extra = tk.Frame(self.root)
        self.extra.grid(row=2, column=1)

        P1 = tk.Label(self.left,text="Player 1 Cards")
        Ex = tk.Label(self.extra,text="Extra")
        P2 = tk.Label(self.right,text="Player 2 Cards")

        #P1.pack(side="left", anchor="w", fill='x')
        #P2.pack(side="right", anchor="e", fill='x')
        P1.grid(row=0,column=0)#, sticky='s')
        Ex.grid(row=0,column=0)
        P2.grid(row=0,column=0)#, sticky='s')

        inc = [0,0,0]
        count = 1
        for card in self.game.cards:
            img = ImageTk.PhotoImage(Image.open(str(count)+".jpg"))
            count+= 1 

            if card.holder == "red":
                row = 0
                target=self.right
            elif card.holder == "blue":
                row = 1
                target=self.left
            else:
                row = 2
                target=self.extra

            inc[row] += 1
            panel = tk.Label(target, image = img)
            panel.photo = img
            panel.grid(row=inc[row],column=0)


        #panel = tk.Label(self.actions, image = img)
        #panel.photo = img

        #panel.grid(row=1,column=0)

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

x = OnitamaGUI()

