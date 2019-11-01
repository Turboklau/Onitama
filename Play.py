from Robots.AssassinAndy import AssassinAndy
from Robots.DirectDerek import DirectDerek
from Robots.ErraticErin import ErraticErin
from Robots.RandomRebecca import RandomRebecca
from Robots.FirstFinley import First_Finley
from Robots.TreeAI import TreeAI

from Game import Game, GUIGame


robot1 = TreeAI(1)
robot2 = TreeAI(1)

#game = GUIGame(robot1, robot2)
game = Game(robot1, robot2)


