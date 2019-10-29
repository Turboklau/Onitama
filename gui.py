import tkinter as tk#, Label, Button
import tkinter.ttk
from OnitamaForRobots import Game


class OnitamaGUI:
    def __init__(self, game):
        self.root = tk.Tk()
        self.game = game
        #print(game.board_state)# [i][j] =
        board = [ [None]*5 for _ in range(5) ]
        for i,row in enumerate(game.board_state):
            for j,col in enumerate(row):
                colour, kind = self.game.get_square(i, j)
                #text = {"master":' M ', "student":' S ', '':'‎‎‎‏‏‎   ‎'}[kind]
                text = {"master":'♕', "student":'♙', '':'‎‎‎‏‏‎ ‎'}[kind]

                L = tk.Label(self.root,text=text,bg=colour, font=('Courier', 128))
                L.grid(row=i,column=j)
                L.bind('<Button-1>',lambda e,i=i,j=j: self.on_click(i,j,e))
                #tk.ttk.Separator(self.root, orient='vertical').grid(column=1, row=0, rowspan=5, sticky='ns')



        self.root.mainloop()

    def on_click(self, i,j,event):
        color = "red"
        event.widget.config(bg=color)

    def pvp(self):
        self.pvp.destroy()


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

