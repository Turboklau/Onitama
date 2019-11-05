import math

from Robots.BaseAI import BaseAI

"""Candice runs away from the enemy pieces"""


class CowardlyCandice(BaseAI):

    def evaluate_points(self, board, me, robotinfo):
        friendly_master = None
        pieces = []
        for piece in board.pieces:
            if piece.player != me:
                pieces.append(piece)
            elif piece.master:
                friendly_master = piece
        return self.total_distance_from_master(pieces, friendly_master)

    def total_distance_from_master(self, pieces, friendly_master):

        total_distance = 0
        for piece in pieces:
            total_distance += self.distance_between_locations(piece.location, friendly_master.location)
        total_distance -= len(pieces)*6
        return total_distance

    def distance_between_locations(self, a, b):
        return math.sqrt((a[0]-b[0])**2 + (a[1]-b[1])**2)