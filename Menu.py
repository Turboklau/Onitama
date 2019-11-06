import tkinter as tk

from PIL import Image, ImageTk

from Game import GUIGame
from Robots.AssassinAndy import AssassinAndy
from Robots.CowardlyCandice import CowardlyCandice
from Robots.DirectDerek import DirectDerek
from Robots.ErraticErin import ErraticErin
from Robots.KillerKyle import KillerKyle
from Robots.LieutenantLarry import LieutenantLarry
from Robots.ParanoidPam import ParanoidPam
from Robots.SadisticSarah import SadisticSarah
from Robots.TacticalTanya import TacticalTanya

robot1 = TacticalTanya(3)
robot2 = LieutenantLarry(4)
robot3 = SadisticSarah()
robot4 = ParanoidPam()
robot5 = DirectDerek()
robot6 = CowardlyCandice()
robot7 = AssassinAndy()
robot8 = ErraticErin()
robot9 = KillerKyle()


class Menu:
    def __init__(self):
        self.root = tk.Tk()
        self.title = tk.Label(self.root, text="Onitama!", font=("Helvetica", 64))
        self.title.grid(row=0,column=1)
        self.create_menu_buttons()
        self.root.mainloop()

    def load_image(self, card):
        img = Image.open("res/" + card + ".png")
        h = int(img.height // 1.5)
        w = int(img.width // 1.5)
        img = img.resize((w, h), Image.ANTIALIAS)
        img = ImageTk.PhotoImage(img)
        return img

    def create_menu_buttons(self):
        f = tk.Frame(self.root)
        f.grid(row=1, column=1)

        b = tk.Button(f, text="Player vs Robot", borderwidth=4, padx=4, pady=4, command=self.player_vs_robot)
        b.grid(row=0, column=0)

        b = tk.Button(f, text="Player vs Player", borderwidth=4, padx=4, pady=4, command=self.player_vs_player)
        b.grid(row=0, column=1)

        b = tk.Button(f, text="Robot vs Robot", borderwidth=4, padx=4, pady=4, command=self.robot_vs_robot)
        b.grid(row=0, column=2)

    def robot_vs_robot(self):
        game = GUIGame(robot1, robot3, self.root, 100)

    def player_vs_robot(self):
        print("player_vs_robot")

    def player_vs_player(self):
        print("player_vs_player")
        game = GUIGame(robot1, robot3, self.root, 100)
