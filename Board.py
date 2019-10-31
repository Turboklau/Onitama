from Piece import Piece

player1 = 0
player2 = 1

color_code_red = '\x1b[0;31;47m'
color_code_blue = '\x1b[0;34;47m'
color_code_black = '\x1b[0;30;47m'
color_code_end = '\x1b[0m'

default_board = ([None, None, None, None, None],
                 [None, None, None, None, None],
                 [None, None, None, None, None],
                 [None, None, None, None, None],
                 [None, None, None, None, None])

class Board:

    def __init__(self):
        self.board_state = list(default_board)
        self.pieces = set()
        self.populate_board()

    def populate_board(self):

        for index, num in enumerate([0, 0, 0, 0, 0, 4, 4, 4, 4, 4]):

            if num == 0:
                piece = Piece(1)
            else:
                piece = Piece(0)

            self.pieces.add(piece)
            piece.location = [num, index%5]
            self.board_state[num][index%5] = piece
            if index%5 == 2:
                piece.master = True

    def is_won(self):
        if isinstance(self.board_state[0][2], Piece) and self.board_state[0][2].player == player1 and self.board_state[0][2].master:
            return True

        if isinstance(self.board_state[4][2], Piece) and self.board_state[4][2].player == player2 and self.board_state[4][2].master:
            return True

        return self.master_captured()

    def master_captured(self):
        num_masters = 0
        for piece in self.pieces:
            if piece.master:
                num_masters += 1
        return num_masters < 2

    def is_possible_move(self, card, player, start, end):
        start_row, start_col = start
        end_row, end_col = end
        piece = self.board_state[start_row][start_col]
        if isinstance(piece, Piece) and self.on_board_and_not_friendly(end_row, end_col, player):
            for move in card.moves:
                if (piece.player == player1 and end == [start_row + move[0], start_col + move[1]]) \
                        or (piece.player == player2 and end == [start_row - move[0], start_col - move[1]]):
                    return True
        return False

    def on_board_and_not_friendly(self, row, col, player):
        if not (0 <= row < len(self.board_state[0]) and 0 <= col < len(self.board_state)):
            return False
        if isinstance(self.board_state[row][col], Piece) and self.board_state[row][col].player == player:
            return False

        return True

    def move_piece(self, start, end):
        start_row, start_col = start
        end_row, end_col = end
        self.remove_piece(end_row, end_col)
        self.board_state[start_row][start_col].location = [end_row, end_col]
        self.board_state[end_row][end_col] = self.board_state[start_row][start_col]
        self.board_state[start_row][start_col] = None

    def remove_piece(self, end_row, end_col):
        if isinstance(self.board_state[end_row][end_col], Piece):
            for piece in self.pieces:
                if piece.location == [end_row, end_col]:
                    piece.location = [-1, -1]
                    self.pieces.remove(piece)
                    return True
        return False

    def print_board(self):
        print()
        for row in self.board_state:
            row_string = ""
            for space in row:
                if isinstance(space, Piece):
                    if space.player == player1:
                        if space.master:
                            row_string += (color_code_red + "mm" + color_code_end)
                        else:
                            row_string += (color_code_red + "ss" + color_code_end)
                    if space.player == player2:
                        if space.master:
                            row_string += (color_code_blue + "mm" + color_code_end)
                        else:
                            row_string += (color_code_blue + "ss" + color_code_end)
                else:
                    row_string += (color_code_black + "[]" + color_code_end)
            print(row_string)
        print()
