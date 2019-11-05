from Game import GUIGame, Game
from Robots.AssassinAndy import AssassinAndy
from Robots.DirectDerek import DirectDerek
from Robots.LieutenantLarry import LieutenantLarry
from Robots.TacticalTanya import TacticalTanya
from Robots.TreeAI import TreeAI
from Robots.ErraticErin import ErraticErin
from Robots.KillerKyle import KillerKyle
from Robots.CowardlyCandice import CowardlyCandice
from Robots.SadisticSarah import SadisticSarah
from Robots.ParanoidPam import ParanoidPam

robot1 = TacticalTanya(4)
robot2 = LieutenantLarry(4)
robot3 = SadisticSarah()
robot4 = ParanoidPam(True)
robot5 = DirectDerek()

game = GUIGame(robot5, robot3)