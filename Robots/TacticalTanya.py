import copy
import math

from Robots.TreeAI import TreeAI

"""Tanya can see the future. Tanya makes moves using a game tree."""
#https://jsfiddle.net/Laa0p1mh/3/

piece_board_values = [
    [-0.5, 0, 0, 0, -0.5],
    [0, 0.5, 1, 0.5, 0],
    [0.5, 1, 1.5, 1, 0.5],
    [0, 0.5, 1, 0.5, 0],
    [-0.5, 0, 0, 0, -0.5]
]

p1_master_board_values = [
    [0, 2, 1000, 2, 0],
    [0, 2, 2, 2, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0]
]

p2_master_board_values = [
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 2, 2, 2, 0],
    [0, 2, 1000, 2, 0]
]

master_board_list = [p1_master_board_values, p2_master_board_values]

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
                score += piece_board_values[piece.location[0]][piece.location[1]]
                if piece.master:
                    friendly_master = True
                    score += master_board_list[root_player][piece.location[0]][piece.location[1]]
                num_friendly += 1
            else:
                score -= piece_board_values[piece.location[0]][piece.location[1]]
                if piece.master:
                    enemy_master = True
                    score -= master_board_list[1-root_player][piece.location[0]][piece.location[1]]
                num_enemy += 1
        if not friendly_master:
            score -= 1000
        if not enemy_master:
            score += 1000
        score += (num_friendly - num_enemy) * 20
        return score