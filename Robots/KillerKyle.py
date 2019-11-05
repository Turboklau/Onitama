
from Robots.BaseAI import BaseAI

"""Kyle drinks monster and kicks holes in walls."""


class KillerKyle(BaseAI):

    def evaluate_points(self, board, me, robotinfo):
        return -len(board.pieces)