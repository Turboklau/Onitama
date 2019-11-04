import copy
import math


"""Tanya can see the future. Tanya makes moves using a game tree."""
#https://jsfiddle.net/Laa0p1mh/3/


class TacticalTanya:

    def __init__(self, color, depth):
        self.color = color
        self.depth = depth

    def decide_move(self, game):
        new_game = copy.deepcopy(game)
        best_state_tuple = self.minimax(new_game, self.depth, -math.inf, math.inf, True)
        best_state = best_state_tuple[1]
        best_state.points = best_state_tuple[0]
        print()
        print()
        print(self.color)
        print(best_state.card.name)
        new_game.print_board(best_state.game_state.board_state)
        print(best_state.points)
        return best_state

    def minimax(self, move_to_be_copied, depth, alpha, beta, maximizing_player):
        move = copy.deepcopy(move_to_be_copied)

        if depth == 0 or self.game_over(move):
            return self.evaluate_points(move), move

        if isinstance(move, Game):
            moves = move.move_list()
        else:
            move.game_state.end_turn()
            moves = move.game_state.move_list()

        if maximizing_player:
            maxEval = -math.inf, None
            for child in moves:
                eval = self.minimax(child, depth-1, alpha, beta, False)
                if eval[0] > maxEval[0]:
                    maxEval = (eval[0], child)
                alpha = max(alpha, eval[0])
                if beta <= alpha:
                    break
            return maxEval

        else:
            minEval = math.inf, None
            for child in moves:
                eval = self.minimax(child, depth-1, alpha, beta, True)
                if eval[0] < minEval[0]:
                    minEval = (eval[0], child)
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
        total_points = 0
        return total_points