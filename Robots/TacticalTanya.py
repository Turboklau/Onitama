import copy
import math

from Robots.TreeAI import TreeAI

"""Tanya can see the future. Tanya makes moves using a game tree."""
#https://jsfiddle.net/Laa0p1mh/3/

board_values = [
    [-1, 0, 0, 0, -1],
    [0, 0.5, 1, 0.5, 0],
    [0.5, 1, 1.5, 1, 0.5],
    [0, 0.5, 1, 0.5, 0],
    [-1, 0, 0, 0, -1]
]

class TacticalTanya(TreeAI):

    def evaluate_points(self, board_state, root_player):
        score = 0
        pieces = board_state[0].pieces
        friendly_master = False
        enemy_master = False
        num_enemy = 0
        num_friendly = 0
        for piece in pieces:
            if piece.player == root_player:
                score += board_values[piece.location[0]][piece.location[1]]
                if piece.master:
                    friendly_master = True
                num_friendly += 1
            else:
                score -= board_values[piece.location[0]][piece.location[1]]
                if piece.master:
                    enemy_master = True
                num_enemy += 1
        if not friendly_master:
            score -= 100
        if not enemy_master:
            score += 120
        score += (num_friendly - num_enemy) * 20
        return score