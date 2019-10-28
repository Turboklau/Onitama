import math
from OnitamaForRobots import Game
from Robots.BaseAI import BaseAI

"""Tanya can see the future. Tanya makes moves using a game tree."""

"""The entire game needs to be passed in to the min/max. It needs to be copied."""

class TacticalTanya(BaseAI):

    def decide_move(self):
        simulated_game = Game(self.game.board_state, self.game.cards, self.game.pieces)
        moves = simulated_game.move_list()
        #start from here
        for move in moves:
            move.points = self.evaluate_points(move)
        best_move = min(moves, key=lambda x: x.points)
        print()
        print()
        print(self.color)
        print(best_move.card.name)
        self.game.print_board(best_move.new_board_state)
        print(best_move.points)
        return best_move

    def evaluate_points(self, move):
        pieces = []
        enemy_master = None
        for piece in self.game.pieces:
            if piece.color == self.color:
                pieces.append(piece)
            elif piece.color != self.color and piece.type == "master":
                enemy_master = piece
        return self.total_distance_from_master(pieces, enemy_master, move.new_board_state)

    def total_distance_from_master(self, pieces, enemy_master, new_board_state):
        total_distance = 0
        master_location = self.game.get_piece_position_on_board(new_board_state, enemy_master)
        if not master_location:
            return 0
        for piece in pieces:
            piece_location = self.game.get_piece_position_on_board(new_board_state, piece)
            if piece_location:
                total_distance += self.distance_between_locations(piece_location, master_location)
        return total_distance


    def distance_between_locations(self, a, b):
        return math.sqrt((a[0]-b[0])**2 + (a[1]-b[1])**2)

    def max_value(self, tree):
        if self.terminal_test(tree):
            return tree
        v = -math.inf
        for s in tree:
            v = max(v, self.min_value(s))
        return v

    def min_value(self, tree):
        if self.terminal_test(tree):
            return tree
        v = math.inf
        for s in tree:
            v = min(v, self.max_value(s))
        return v

    def terminal_test(self, state):
        return not isinstance(state, list)

    def max_action_value(self, game_tree):
        x = None
        if self.terminal_test(game_tree):
            return x, game_tree
        v = -math.inf
        for i in range(0, len(game_tree)):
            if v < self.min_value(game_tree[i]):
                v = max(v, self.min_value(game_tree[i]))
                x = i
        return x, v

    def min_action_value(self, game_tree):
        x = None
        if self.terminal_test(game_tree):
            return x, game_tree
        v = math.inf

        for i in range(0, len(game_tree)):
            if v > self.max_value(game_tree[i]):
                v = min(v, self.max_value(game_tree[i]))
                x = i
        return x, v