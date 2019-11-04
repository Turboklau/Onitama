
from Robots.BaseAI import BaseAI

"""Andy minimises the total distance between his pieces and the enemy master."""


class KillerKyle(BaseAI):

    def evaluate_points(self, board, me):
        return -len(board.pieces)