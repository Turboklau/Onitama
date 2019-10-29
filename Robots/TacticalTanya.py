import math
import random

from OnitamaForRobots import Game, Move

"""Tanya can see the future. Tanya makes moves using a game tree."""

"""The entire game needs to be passed in to the min/max. It needs to be copied."""

class TacticalTanya():

    def __init__(self, game, color, depth):
        self.game = game
        self.color = color
        self.depth = depth

    def decide_move(self):
        best_state_tuple = self.minimax(self.game, self.depth, -math.inf, math.inf, True)
        best_state = best_state_tuple[1]
        best_state.points = best_state_tuple[0]
        print()
        print()
        print(self.color)
        print(best_state.card.name)
        self.game.print_board(best_state.game_state.board_state)
        print(best_state.points)
        return best_state

    def minimax(self, move, depth, alpha, beta, maximizing_player):

        if depth == 0 or self.game_over(move):
            return self.evaluate_points(move), move

        if isinstance(move, Game):
            moves = move.move_list()
        else:
            moves = move.game_state.move_list()

        if maximizing_player:
            maxEval = -math.inf, None
            for child in moves:
                eval = self.minimax(child, depth-1, alpha, beta, False)
                if eval[0] >= maxEval[0]:
                    maxEval = eval
                alpha = max(alpha, eval[0])
                if beta <= alpha:
                    break
            return maxEval

        else:
            minEval = math.inf, None
            for child in moves:
                eval = self.minimax(child, depth-1, alpha, beta, True)
                if eval[0] <= minEval[0]:
                    minEval = eval
                beta = min(beta, eval[0])
                if beta <= alpha:
                    break
            return minEval

    def game_over(self, move):
        if isinstance(move, Game):
            return move.is_won()
        else:
            return move.game_state.is_won()

    def evaluate_points(self, move):
        print("eval")
        total_points = 0
        if isinstance(move, Game):
            return -1
        else:
            friendly_master_dead = True
            enemy_master_dead = True
            for piece in move.game_state.pieces:
                if piece.type == "master":
                    if piece.color == self.color:
                        friendly_master_dead = False
                    if piece.color != self.color:
                        enemy_master_dead = False
            if enemy_master_dead:
                total_points += 110
            if friendly_master_dead:
                total_points -= 100
        return total_points