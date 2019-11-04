from Game import GUIGame
from Robots.DirectDerek import DirectDerek
from Robots.TreeAI import TreeAI
from Robots.ErraticErin import ErraticErin
from Robots.KillerKyle import KillerKyle
from Robots.CowardlyCandice import CowardlyCandice
from Robots.SadisticSarah import SadisticSarah
from Robots.ParanoidPam import ParanoidPam

robot1 = CowardlyCandice()
robot2 = KillerKyle()
robot3 = SadisticSarah()
robot4 = ParanoidPam()

#Red, Blue
game = GUIGame(robot2, robot4)