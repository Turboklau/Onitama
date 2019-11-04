import copy
import math
import random

from Piece import Piece

board_values = [
    [-1, 0, 0, 0, -1],
    [0, 0.5, 1, 0.5, 0],
    [0.5, 1, 1.5, 1, 0.5],
    [0, 0.5, 1, 0.5, 0],
    [-1, 0, 0, 0, -1]
]
"""
What's better than two AIs?
Need to sort out the cards with the min max tree stuff
"""


class TreeAI:

    def __init__(self, depth):
        self.depth = depth

    def decide_move(self, robotInfo):
        # Inverts movement matrix if playing for opposing side

        me = robotInfo.get_me()
        board = robotInfo.get_board_class()
        me_hand = robotInfo.get_hand(me)
        you_hand = robotInfo.get_hand(1-me)
        mid_card = robotInfo.get_mid_card()

        best_move_card = None
        best_move_start = None
        best_move_end = None
        best_move_points = -math.inf
        isMaximisingPlayer = True

        new_board_states = self.get_new_board_states(board, me, me_hand, mid_card)

        for i in range(0, len(new_board_states)):
            new_board_state = new_board_states[i]
            points = self.minimax(self.depth - 1, new_board_state, -math.inf, math.inf, not isMaximisingPlayer, 1-me)
            if points >= best_move_points:
                best_move_points = points
                best_move_card = new_board_state[2]
                best_move_start = new_board_state[3]
                best_move_end = new_board_state[4]

        print("Player " + str(me + 1) + ": " + best_move_card.name + " worth " + str(best_move_points))
        return best_move_card, best_move_start, best_move_end


    def get_new_board_states(self, board, me, me_hand, mid_card):
        mult = 1
        if me == 1:
            mult = -1

        board_states = []
        for card_index in range(0, len(me_hand)):
            # For every move
            for move in me_hand[card_index].moves:
                # For every piece of mine
                for piece in board.pieces:
                    if piece.player == me:
                        start = piece.location
                        end = [start[0] + mult * move[0],
                               start[1] + mult * move[1]]
                        if board.is_possible_move(me_hand[card_index], me, start, end):
                            new_board = robotInfo.get_board_class()
                            me_hand = robotInfo.get_hand(me)
                            you_hand = robotInfo.get_hand(1 - me)
                            mid_card = robotInfo.get_mid_card()

                            board.board_state.move_piece(start, end)
                            board_states.append((board, players, mid_card, start, end))

        return board_states

    def dirty_swap(self, players, me, card, mid_card):
        if players[me].hand[0] == card:
            players[me].hand[0], mid_card = mid_card, players[me].hand[0]

        elif players[me].hand[1] == card:
            players[me].hand[1], mid_card = mid_card, players[me].hand[1]

    def minimax(self, depth, board_state, alpha, beta, isMaximisingPlayer, me):
        if depth == 0:
            return self.evaluate_points(board_state, me)

        new_board_states = self.get_new_board_states(board_state[0], me, board_state[1], board_state[2])

        if isMaximisingPlayer:
            best_move_points = -math.inf
            for i in range(0, len(new_board_states)):
                new_board_state = new_board_states[i]
                points = self.minimax(depth - 1, new_board_state, -math.inf, math.inf, not isMaximisingPlayer, 1 - me)
                best_move_points = max(points, best_move_points)
                alpha = max(alpha, best_move_points)
                if beta <= alpha:
                    break
            return best_move_points

        else:
            best_move_points = -math.inf
            for i in range(0, len(new_board_states)):
                new_board_state = new_board_states[i]
                points = self.minimax(depth - 1, new_board_state, -math.inf, math.inf, not isMaximisingPlayer, 1 - me)
                best_move_points = max(points, best_move_points)
                beta = min(alpha, best_move_points)
                if beta <= alpha:
                    break
            return best_move_points


    def evaluate_points(self, board_state, me):
        score = 0
        pieces = board_state[0].pieces
        friendly_master = False
        enemy_master = False
        for piece in pieces:
            if piece.player == me:
                score += board_values[piece.location[0]][piece.location[1]]
                if piece.master:
                    friendly_master = True
            else:
                score -= board_values[piece.location[0]][piece.location[1]]
                if piece.master:
                    enemy_master = True

        if not friendly_master:
            score -= 100
        if not enemy_master:
            score += 120
        return score