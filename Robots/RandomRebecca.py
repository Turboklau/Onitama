import random

from Robots.BaseAI import BaseAI

"""Rebecca randomly chooses a move and takes it."""

class RandomRebecca(BaseAI):

    def evaluate_points(self, move):
        return random.randint(0, 1000)