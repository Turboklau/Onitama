import math

from Robots.BaseAI import BaseAI

"""Derek minimises the distance between his master and the enemy shrine."""

class DirectDerek(BaseAI):

    def evaluate_points(self, board, me):
        friendly_master = None
        for piece in board.pieces:
            if piece.player == me and piece.master:
                friendly_master = piece
        return -self.total_distance_from_enemy_shrine(friendly_master)

    def total_distance_from_enemy_shrine(self, friendly_master):
        if not friendly_master:
            return math.inf
        if friendly_master.player == 1:
            return self.distance_between_locations(friendly_master.location, (4, 2))
        else:
            return self.distance_between_locations(friendly_master.location, (0, 2))

    def distance_between_locations(self, a, b):
        return math.sqrt((a[0]-b[0])**2 + (a[1]-b[1])**2)