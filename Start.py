from Robots.AssassinAndy import AssassinAndy
from Robots.DirectDerek import DirectDerek
from Robots.ErraticErin import ErraticErin
from Robots.RandomRebecca import RandomRebecca
from Robots.FirstFinley import FirstFinley
from Robots.TreeAI import TreeAI

from Game import Game, GUIGame


robot1 = FirstFinley()
robot2 = FirstFinley()

game = GUIGame(robot1, robot2)
#game = Game(robot1, robot2)


