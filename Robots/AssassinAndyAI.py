import math

from Robots.BaseAI import BaseAI

"""Andy minimises the total distance between his pieces and the enemy master."""

class AssassinAndyAI(BaseAI):

    def evaluate_points(self, move):
        pieces = []
        enemy_master = None
        for piece in move.game_state.pieces:
            if piece.color == self.color:
                pieces.append(piece)
            elif piece.color != self.color and piece.type == "master":
                enemy_master = piece
        return -self.total_distance_from_master(pieces, enemy_master, move.game_state)

    def total_distance_from_master(self, pieces, enemy_master, game_state):
        total_distance = 0
        master_location = game_state.get_piece_position_on_board(game_state.board_state, enemy_master)
        if not master_location:
            return -math.inf
        for piece in pieces:
            piece_location = game_state.get_piece_position_on_board(game_state.board_state, piece)
            if piece_location:
                total_distance += self.distance_between_locations(piece_location, master_location)
        return total_distance


    def distance_between_locations(self, a, b):
        return math.sqrt((a[0]-b[0])**2 + (a[1]-b[1])**2)