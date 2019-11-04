
import copy
import math


class BaseAI():

    def __init__(self):
        pass

    def decide_move(self, robotinfo):
        # Inverts movement matrix if playing for opposing side

        me = robotinfo.get_me()
        board = robotinfo.get_board_class()

        mult = 1
        if me == 1:
            mult = -1

        best_move_card = None
        best_move_start = None
        best_move_end = None
        best_move_points = -math.inf

        my_hand = robotinfo.get_hand(me)
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
                            points = self.evaluate_points(dirty_board, me, robotinfo)
                            if points > best_move_points:
                                best_move_card, best_move_start, best_move_end, best_move_points = card, start, end, points

        if best_move_card and best_move_start and best_move_end:
            print("Player " + str(me + 1) + ": " + best_move_card.name)
            return best_move_card, best_move_start, best_move_end
        else:
            print("No available moves")

    def evaluate_points(self, board, me, players):
        return 0
