import math
import random

from Piece import Piece
from Robots.BaseAI import BaseAI

"""Erin randomly chooses a move and takes it, unless a winning move is available, then she takes that instead."""

class ErraticErin(BaseAI):

    def evaluate_points(self, board, me, players):
        winning_move = True
        for row in board.board_state:
            for space in row:
                if isinstance(space, Piece) and space.master and space.player != me:
                    winning_move = False
        blue_shrine = board.board_state[4][2]
        red_shrine = board.board_state[0][2]
        if me == 1:
            if isinstance(blue_shrine, Piece) and blue_shrine.player == me and blue_shrine.master:
                winning_move = True
        if me == 0:
            if isinstance(red_shrine, Piece) and red_shrine.player == me and red_shrine.master:
                winning_move = True
        if winning_move:
            return math.inf
        else:
            return random.randint(1, 1000)