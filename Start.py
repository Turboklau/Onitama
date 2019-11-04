from Game import GUIGame
from Robots.AssassinAndy import AssassinAndy
from Robots.DirectDerek import DirectDerek
from Robots.TreeAI import TreeAI
from Robots.ErraticErin import ErraticErin
from Robots.KillerKyle import KillerKyle
from Robots.CowardlyCandice import CowardlyCandice

robot1 = CowardlyCandice()
robot2 = KillerKyle()

game = GUIGame(robot1, robot2)