from Game import GUIGame, Game
from Robots.AssassinAndy import AssassinAndy
from Robots.DirectDerek import DirectDerek
from Robots.TreeAI import TreeAI
from Robots.ErraticErin import ErraticErin
from Robots.KillerKyle import KillerKyle
from Robots.CowardlyCandice import CowardlyCandice
from Robots.SadisticSarah import SadisticSarah
from Robots.ParanoidPam import ParanoidPam

robot1 = TreeAI(2)
robot2 = DirectDerek()
robot3 = SadisticSarah()
robot4 = ParanoidPam(True)

game = Game(robot1, robot2)