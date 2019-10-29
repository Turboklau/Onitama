import tkinter as tk#, Label, Button
import tkinter.ttk
from OnitamaForRobots import Game


class OnitamaGUI:
    def __init__(self, game):
        self.root = tk.Tk()
        self.game = game
        self.title = tk.Label(self.root,text="Today is Onitama", font=('Courier', 128))
        self.title.grid(row=0,column=0)

        self.board = tk.Frame(self.root)
        self.board.grid(row=1,column=0)

        self.actions = tk.Frame(self.root)
        self.actions.grid(row=2,column=0)
        
        self.update_board()
        self.update_actions()



        self.root.mainloop()

    def on_click(self, i,j,event):
        color = "red"
        event.widget.config(bg=color)

    def pvp(self):
        self.pvp.destroy()



    def update_board(self):
        board = [ [None]*5 for _ in range(5) ]
        for i,row in enumerate(game.board_state):
            for j,col in enumerate(row):
                colour, kind = self.game.get_square(i, j)
                text = {"master":' M ', "student":' S ', '':'‎‎‎‏‏‎   ‎'}[kind]
                #text = {"master":'♕', "student":'♙', '':'‎‎‎‏‏‎ ‎'}[kind]

                L = tk.Label(self.board,text=text,bg=colour, font=('Courier', 128))
                L.grid(row=i,column=j)
                L.bind('<Button-1>',lambda e,i=i,j=j: self.on_click(i,j,e))
                #tk.ttk.Separator(self.root, orient='vertical').grid(column=1, row=0, rowspan=5, sticky='ns')

    def update_actions(self):
        for card in self.game.cards:
            print(card)
        P1 = tk.Label(self.actions,text="P1 Cardfdggrgrrgrgrgrgrgrgrs", bg="green")
        Ex = tk.Label(self.actions,text="Extra")
        P2 = tk.Label(self.actions,text="P2 Cards")

        #P1.pack(side="left", anchor="w", fill='x')
        #P2.pack(side="right", anchor="e", fill='x')
        P1.grid(row=0,column=0, sticky="w")
        #Ex.grid(row=0,column=1, sticky)
        P2.grid(row=0,column=2, sticky="e")



def main():
    print("\nWelcome to Onitama! This is a 2 player game similar to chess.")
    #game.set_up()
    #if mode == "1":
    #    pvp_loop(game)
    #elif mode == "2":
    #    robot1 = get_robot('erin', game, 'red')
    #    pve_loop(robot1, game)
    #elif mode == "3":
    #    robot1 = get_robot('derek', game, 'red')
    #    robot2 = get_robot('derek', game, 'blue')
    #    robot_battle_loop(robot1, robot2, game)#

    #print("winner is " + game.current_player)


#root = tk.Tk()
#my_gui = OnitamaGUI(root)
#root.mainloop()
#main()


game = Game()
x = OnitamaGUI(game)

    #board[i][j] = color

