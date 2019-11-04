import math

from Robots.BaseAI import BaseAI

"""Andy minimises the total distance between his pieces and the enemy master."""


class CowardlyCandice(BaseAI):

    def evaluate_points(self, board, me, players):
        enemy_master = None
        pieces = []
        for piece in board.pieces:
            if piece.player == me:
                pieces.append(piece)
            elif piece.master:
                enemy_master = piece
        return self.total_distance_from_master(pieces, enemy_master)

    def total_distance_from_master(self, pieces, enemy_master):
        total_distance = 0
        if not enemy_master:
            return -math.inf
        for piece in pieces:
            total_distance += self.distance_between_locations(piece.location, enemy_master.location)
        return total_distance

    def distance_between_locations(self, a, b):
        return math.sqrt((a[0]-b[0])**2 + (a[1]-b[1])**2)