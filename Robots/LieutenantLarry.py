import copy
import math

from Robots.TreeAI import TreeAI

"""Lieutenant Larry doesn't care about positioning as long as he can take pieces. Also, he would rather trade
pieces than live in peace."""

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

class LieutenantLarry(TreeAI):

    def evaluate_points(self, board_state, root_player):
        score = 0
        pieces = board_state[0].pieces
        friendly_master = False
        enemy_master = False
        num_enemy = 0
        num_friendly = 0
        for piece in pieces:
            if piece.player == root_player:
                if piece.master:
                    friendly_master = True
                    score += master_board_list[root_player][piece.location[0]][piece.location[1]]
                num_friendly += 1
            else:
                if piece.master:
                    enemy_master = True
                    score -= master_board_list[1-root_player][piece.location[0]][piece.location[1]]
                num_enemy += 1
        if not friendly_master:
            score -= 1000
        if not enemy_master:
            score += 1000
        score -= num_enemy*3
        score += num_friendly*3
        score += (10 - (num_enemy+num_friendly))
        return score