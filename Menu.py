import tkinter as tk
from tkinter import ttk
import logging
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

ROBOT_DICT = {'tanya': TacticalTanya(3), 'larry': LieutenantLarry(3), 'sarah': SadisticSarah(),
              'pam': ParanoidPam(), 'derek': DirectDerek(), 'candice': CowardlyCandice(),
              'andy': AssassinAndy(), 'erin': ErraticErin(), 'kyle': KillerKyle()}


class Menu:
    def __init__(self):
        self.root = tk.Tk()
        self.title = tk.Label(self.root, text="Onitama!", font=("Helvetica", 64))
        self.title.grid(row=1, column=1)
        self.create_menu_buttons(self.root)
        self.root.mainloop()

    def load_image(self, card):
        img = Image.open("res/" + card + ".png")
        h = int(img.height // 1.5)
        w = int(img.width // 1.5)
        img = img.resize((w, h), Image.ANTIALIAS)
        img = ImageTk.PhotoImage(img)
        return img

    def create_menu_buttons(self, root):
        f = tk.Frame(root)
        f.grid(row=2, column=1)

        robot_select1 = ttk.Combobox(f, values=list(ROBOT_DICT.keys()), state='readonly')
        robot_select1.grid(row=1, column=0)
        robot_select1.current(0)

        human_checkbox1 = tk.Checkbutton(f, text="Human", borderwidth=4, padx=4, pady=4, command=lambda: self.disable(0))
        human_checkbox1.grid(row=0, column=0)

        robot_select2 = ttk.Combobox(f, values=list(ROBOT_DICT.keys()), state='readonly')
        robot_select2.grid(row=1, column=2)
        robot_select2.current(0)

        human_checkbox2 = tk.Checkbutton(f, text="Human", borderwidth=4, padx=4, pady=4, command=lambda: self.disable(2))
        human_checkbox2.grid(row=0, column=2)

        go = tk.Button(f, text="START", borderwidth=4, padx=4, pady=4, command=self.play)
        go.grid(row=2, column=0, columnspan=3)

    def robot_vs_robot(self, robot_player1, robot_player2):
        game = GUIGame(robot_player1, robot_player2, self.root, 100)

    def player_vs_robot(self):
        print("player_vs_robot")

    def player_vs_player(self):
        print("player_vs_player")
        # game = GUIGame(robot1, robot3, self.root, 100)

    def disable(self, combo_id):
        frame = self.root.winfo_children()[1]
        combobox = frame.winfo_children()[combo_id]
        if str(combobox['state']) == 'readonly':
            combobox['state'] = 'disabled'
        else:
            combobox['state'] = 'readonly'

    def play(self):
        frame = self.root.winfo_children()[1]
        combobox1 = frame.winfo_children()[0]
        combobox2 = frame.winfo_children()[2]
        robot1 = ROBOT_DICT[combobox1.get()]
        robot2 = ROBOT_DICT[combobox2.get()]

        frame.destroy()

        game = GUIGame(robot1, robot2, self.root)

