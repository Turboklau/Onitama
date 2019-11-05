import copy
import math
import random

from Card import Card
from Piece import Piece

board_values = [
    [-1, 0, 0, 0, -1],
    [0, 0.5, 1, 0.5, 0],
    [0.5, 1, 1.5, 1, 0.5],
    [0, 0.5, 1, 0.5, 0],
    [-1, 0, 0, 0, -1]
]

names = "tiger dragon frog rabbit crab elephant goose rooster monkey mantis horse ox crane boar eel cobra".split()
moves = [
    [(-2, 0), (1, 0)],
    [(-1, -2), (-1, 2), (1, -1), (1, 1)],
    [(-1, -1), (0, -2), (1, 1)],
    [(-1, 1), (0, 2), (1, -1)],
    [(-1, 0), (0, -2), (0, 2)],
    [(-1, -1), (-1, 1), (0, -1), (0, 1)],
    [(-1, -1), (0, -1), (0, 1), (1, 1)],
    [(-1, 1), (0, -1), (0, 1), (1, -1)],
    [(-1, -1), (-1, 1), (1, -1), (1, 1)],
    [(-1, -1), (-1, 1), (1, 0)],
    [(-1, 0), (0, -1), (1, 0)],
    [(-1, 0), (0, 1), (1, 0)],
    [(-1, 0), (1, -1), (1, 1)],
    [(-1, 0), (0, -1), (0, 1)],
    [(-1, -1), (0, 1), (1, -1)],
    [(-1, 1), (0, -1), (1, 1)]
    ]
card_dict = dict()

for i in range(0, len(names)):
    card_dict[names[i]] = Card(names[i], moves[i])


"""
What's better than two AIs? TreeAIs
Need to sort out the cards with the min max tree stuff
"""


class TreeAI:

    def __init__(self, depth):
        self.depth = depth

    def decide_move(self, robotInfo):
        # Inverts movement matrix if playing for opposing side

        me = robotInfo.get_me()
        board = robotInfo.get_board_class()
        mid_card = robotInfo.get_mid_card()
        player_hands = [None, None]
        player_hands[me] = robotInfo.get_hand(me)
        player_hands[1-me] = robotInfo.get_hand(1-me)

        best_move_card = None
        best_move_start = None
        best_move_end = None
        best_move_points = -math.inf

        new_board_states = self.get_new_board_states(board, me, player_hands, mid_card)

        for i in range(0, len(new_board_states)):
            new_board_state = new_board_states[i]
            points = self.minimax(self.depth - 1, new_board_state, -math.inf, math.inf, 1-me, me)
            if points >= best_move_points:
                best_move_points = points
                best_move_card = new_board_state[2]
                best_move_start = new_board_state[3]
                best_move_end = new_board_state[4]

        print("Player " + str(me + 1) + ": " + best_move_card.name + " worth " + str(best_move_points))
        return best_move_card, best_move_start, best_move_end

    def get_new_board_states(self, board, me, player_hands, mid_card):
        mult = 1
        if me == 1:
            mult = -1

        board_states = []
        for card_index in range(0, len(player_hands[me])):
            # For every move
            for move in player_hands[me][card_index].moves:
                # For every piece of mine
                for piece in board.pieces:
                    if piece.player == me:
                        start = piece.location
                        end = [start[0] + mult * move[0],
                               start[1] + mult * move[1]]
                        if board.is_possible_move(player_hands[me][card_index], me, start, end):

                            new_hands = [[None, None], [None, None]]

                            new_hands[me][0] = card_dict.get(player_hands[me][0].name)
                            new_hands[me][1] = card_dict.get(player_hands[me][1].name)
                            new_hands[1-me][0] = card_dict.get(player_hands[1-me][0].name)
                            new_hands[1-me][1] = card_dict.get(player_hands[1-me][1].name)

                            new_mid = card_dict.get(player_hands[me][card_index].name)

                            new_hands[me][card_index] = card_dict.get(mid_card.name)

                            new_board = copy.deepcopy(board)
                            new_board.move_piece(start, end)

                            board_states.append((new_board, new_hands, new_mid, start, end))

        return board_states

    def minimax(self, depth, board_state, alpha, beta, player, root_player):
        if depth == 0 or board_state[0].is_won():
            points = self.evaluate_points(board_state, root_player)
            return points

        new_board_states = self.get_new_board_states(board_state[0], player, board_state[1], board_state[2])

        if player == root_player:
            best_move_points = -math.inf
            for i in range(0, len(new_board_states)):
                new_board_state = new_board_states[i]
                points = self.minimax(depth-1, new_board_state, -math.inf, math.inf, 1-player, root_player)
                best_move_points = max(points, best_move_points)
                alpha = max(alpha, best_move_points)
                if beta <= alpha:
                    break
            return best_move_points

        else:
            best_move_points = math.inf
            for i in range(0, len(new_board_states)):
                new_board_state = new_board_states[i]
                points = self.minimax(depth-1, new_board_state, -math.inf, math.inf, 1-player, root_player)
                best_move_points = min(points, best_move_points)
                beta = min(beta, best_move_points)
                if beta <= alpha:
                    break
            return best_move_points


    def evaluate_points(self, board_state, root_player):
        score = 0
        pieces = board_state[0].pieces
        friendly_master = False
        enemy_master = False
        num_enemy = 0
        num_friendly = 0
        for piece in pieces:
            if piece.player == root_player:
                score += board_values[piece.location[0]][piece.location[1]]
                if piece.master:
                    friendly_master = True
                num_friendly += 1
            else:
                score -= board_values[piece.location[0]][piece.location[1]]
                if piece.master:
                    enemy_master = True
                num_enemy += 1
        if not friendly_master:
            score -= 100
        if not enemy_master:
            score += 120
        score += (num_friendly - num_enemy) * 20
        return score