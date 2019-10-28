import math
import random

from OnitamaForRobots import Piece
from Robots.BaseAI import BaseAI

"""Erin randomly chooses a move and takes it, unless a winning move is available, then she takes that instead."""

class ErraticErin(BaseAI):

    def evaluate_points(self, move):
        winning_move = True
        for row in move.new_board_state:
            for space in row:
                if isinstance(space, Piece) and space.type == "master" and space.color != self.color:
                    winning_move = False
        blue_shrine = move.new_board_state[4][2]
        red_shrine = move.new_board_state[0][2]
        if self.color == "red":
            if isinstance(blue_shrine, Piece) and blue_shrine.color == self.color and blue_shrine.type == "master":
                winning_move = True
        if self.color == "blue":
            if isinstance(red_shrine, Piece) and red_shrine.color == self.color and red_shrine.type == "master":
                winning_move = True
        if winning_move:
            return 0
        else:
            return random.randint(1, 1000)