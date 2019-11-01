import copy
import math


class TreeAI:

    def __init__(self, depth):
        self.depth = depth

    def decide_move(self, board, me, players, mid_card):
        # Inverts movement matrix if playing for opposing side


        best_move_card = None
        best_move_start = None
        best_move_end = None
        best_move_points = -math.inf
        isMaximisingPlayer = True

        new_board_states = self.get_new_board_states(board, me, players, mid_card)

        for i in range(0, len(new_board_states)):
            new_board_state = new_board_states[i]
            points = self.minimax(self.depth - 1, new_board_state, -math.inf, math.inf, not isMaximisingPlayer, 1-me)
            if points >= best_move_points:
                best_move_points = points
                best_move_card = new_board_state[2]
                best_move_start = new_board_state[3]
                best_move_end = new_board_state[4]
        return best_move_card, best_move_start, best_move_end

    def get_new_board_states(self, board, me, players, mid_card):
        mult = 1
        if me == 1:
            mult = -1

        board_states = []
        for card in players[me].hand:
            # For every move
            for move in card.moves:
                # For every piece of mine
                for piece in board.pieces:
                    if piece.player == me:
                        start = piece.location
                        end = [start[0] + mult * move[0],
                               start[1] + mult * move[1]]
                        if board.is_possible_move(card, me, start, end):
                            dirty_board = copy.deepcopy(board)
                            dirty_players = copy.deepcopy(players)
                            dirty_mid_card = copy.deepcopy(mid_card)
                            self.dirty_swap(dirty_players, me, card, dirty_mid_card)
                            dirty_board.move_piece(start, end)
                            board_states.append((dirty_board, dirty_players, dirty_mid_card, start, end))

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
                points = self.minimax(self.depth - 1, new_board_state, -math.inf, math.inf, not isMaximisingPlayer, 1 - me)
                best_move_points = max(points, best_move_points)
                alpha = max(alpha, best_move_points)
                if beta <= alpha:
                    break
            return best_move_points

        else:
            best_move_points = -math.inf
            for i in range(0, len(new_board_states)):
                new_board_state = new_board_states[i]
                points = self.minimax(self.depth - 1, new_board_state, -math.inf, math.inf, not isMaximisingPlayer, 1 - me)
                best_move_points = max(points, best_move_points)
                beta = min(alpha, best_move_points)
                if beta <= alpha:
                    break
            return best_move_points


    def evaluate_points(self, board, me):
        return 0