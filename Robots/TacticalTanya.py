import math
import random

from OnitamaForRobots import Game
from Robots.BaseAI import BaseAI

"""Tanya can see the future. Tanya makes moves using a game tree."""

"""The entire game needs to be passed in to the min/max. It needs to be copied."""

class TacticalTanya():

    def __init__(self, game, color, depth):
        self.game = game
        self.color = color
        self.depth = depth

    def decide_move(self):
        max_player = False
        if self.game.current_player == self.color:
            max_player = True
        return self.minimax(self.game, self.depth, -math.inf, math.inf, max_player)

    def minimax(self, move, depth, alpha, beta, maximizing_player):

        if depth == 0 or self.game_over(move):
            return self.evaluate_points(move)

        if isinstance(move, Game):
            moves = move.move_list()
        else:
            moves = move.game_state.move_list()

        if maximizing_player:
            maxEval = -math.inf
            for move in moves:
                eval = self.minimax(move, depth-1, alpha, beta, False)
                maxEval = max(maxEval, eval)
                alpha = max(alpha, eval)
                if beta <= alpha:
                    break
            return maxEval

        else:
            minEval = math.inf
            for move in moves:
                eval = self.minimax(move, depth-1, alpha, beta, True)
                minEval = min(minEval, eval)
                beta = min(alpha, eval)
                if beta <= alpha:
                    break
            return minEval

    def game_over(self, move):
        if isinstance(move, Game):
            return move.is_won()
        else:
            return move.game_state.is_won()

    def evaluate_points(self, move):
        return random.randint(0, 1000)