from Game import GUIGame
from Robots.DirectDerek import DirectDerek
from Robots.TreeAI import TreeAI

robot1 = DirectDerek()
robot2 = TreeAI(3)

game = GUIGame(robot1, robot2)