from Robots.AssassinAndy import AssassinAndy
from Robots.DirectDerek import DirectDerek
from Robots.ErraticErin import ErraticErin
from Robots.RandomRebecca import RandomRebecca
from Robots.FirstFinley import First_Finley

from Game import Game, GUIGame


robot1 = AssassinAndy()
robot2 = ErraticErin()

game = GUIGame(robot1, robot2)
#game = Game(robot1, robot2)


