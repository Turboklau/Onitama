import math

from Robots.BaseAI import BaseAI

"""Derek minimises the distance between his master and the enemy shrine."""

class DirectDerek(BaseAI):

    def evaluate_points(self, move):
        friendly_master = None
        for piece in move.piece_list:
            if piece.color == self.color and piece.type == "master":
                friendly_master = piece
        return self.total_distance_from_enemy_shrine(friendly_master, move.new_board_state)

    def total_distance_from_enemy_shrine(self, friendly_master, new_board_state):
        total_distance = 0
        master_location = self.game.get_piece_position_on_board(new_board_state, friendly_master)
        if not master_location:
            return 0
        if friendly_master.color == "red":
            return self.distance_between_locations(master_location, (4, 2))
        else:
            return self.distance_between_locations(master_location, (0, 2))


    def distance_between_locations(self, a, b):
        return math.sqrt((a[0]-b[0])**2 + (a[1]-b[1])**2)