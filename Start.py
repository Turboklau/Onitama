from Game import GUIGame, Game
from Robots.AssassinAndy import AssassinAndy
from Robots.DirectDerek import DirectDerek
from Robots.TacticalTanya import TacticalTanya
from Robots.TreeAI import TreeAI
from Robots.ErraticErin import ErraticErin
from Robots.KillerKyle import KillerKyle
from Robots.CowardlyCandice import CowardlyCandice
from Robots.SadisticSarah import SadisticSarah
from Robots.ParanoidPam import ParanoidPam
from Robots.RandomRebecca import RandomRebecca

robot1 = TacticalTanya(2)
robot0 = TacticalTanya(1)
#robot10 = TacticalTanya(0)

robot2 = KillerKyle()
robot3 = SadisticSarah()
robot4 = ParanoidPam()
robot5 = DirectDerek()
robot6 = CowardlyCandice()
robot7 = AssassinAndy()
robot8 = ErraticErin()
robot8 = RandomRebecca()


game = GUIGame(robot0, robot1, battles=100)