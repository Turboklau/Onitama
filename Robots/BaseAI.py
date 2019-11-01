"""There are several ways to motivate the AI:
1: Minimum distance between its own pieces and enemy pieces << This is easy but not really a win condition
2: Minimum distance between its own pieces and enemy master << Assassin Andy
3: Minimum distance between its own master and enemy shrine << Suicide Sam
4: Maximum distance between its own master and enemy pieces
5: Maximum distance between its own shrine and enemy master << This is hard to do with a depth of 1
6: Maximum difference in number of pieces
7: Being in the winning state (i.e. if there is a move that wins, take it)
"""
import copy
import math


class BaseAI():

    def __init__(self):
        pass

    def decide_move(self, board, me, players, mid_card):
        # Inverts movement matrix if playing for opposing side

        mult = 1
        if me == 1:
            mult = -1

        best_move_card = None
        best_move_start = None
        best_move_end = None
        best_move_points = -math.inf

        my_hand = players[me].hand
        # For every card
        for card in my_hand:
            # For every move
            for move in card.moves:
                # For every piece of mine
                for piece in board.pieces:
                    if piece.player == me:
                        # Is that move possible? If so, take it
                        start = piece.location
                        end = [start[0] + mult * move[0],
                               start[1] + mult * move[1]]
                        if board.is_possible_move(card, me, start, end):
                            dirty_board = copy.deepcopy(board)
                            dirty_board.move_piece(start, end)
                            points = self.evaluate_points(dirty_board, me)
                            if points > best_move_points:
                                best_move_card, best_move_start, best_move_end, best_move_points = card, start, end, points

        if best_move_card and best_move_start and best_move_end:
            print("Player " + str(me + 1) + ": " + best_move_card.name)
            return best_move_card, best_move_start, best_move_end
        else:
            print("No available moves")

    def evaluate_points(self, board, me):
        return 0