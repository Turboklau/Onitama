from unittest import TestCase

from Board import Board
from Card import Card
from Piece import Piece


class TestBoard(TestCase):

    def setUp(self):
        self.board = Board()

    def test_populate_board(self):
        self.assertEqual(len(self.board.pieces), 10)
        num_students = 0
        num_masters = 0
        num_red = 0
        num_blue = 0
        for piece in self.board.pieces:
            if piece.master:
                num_masters += 1
            else:
                num_students += 1
            if piece.player == 0:
                num_red += 1
            elif piece.player == 1:
                num_blue += 1

        self.assertEqual(num_masters, 2)
        self.assertEqual(num_students, 8)
        self.assertEqual(num_red, 5)
        self.assertEqual(num_blue, 5)

        self.assertEqual(len(self.board.board_state), 5)
        self.assertEqual(len(self.board.board_state[0]), 5)

        for i in range(0, 5, 4):
            for j in range(0, 5):
                self.assertIs(Piece, type(self.board.board_state[i][j]))

    def test_is_won(self):
        self.assertFalse(self.board.is_won())

        red_master = Piece(0, [0, 2], True)
        blue_master = Piece(1, [4, 2], True)

        self.board.board_state[0][2] = red_master
        self.assertTrue(self.board.is_won())

        self.board = Board()

        self.board.board_state[4][2] = blue_master
        self.assertTrue(self.board.is_won())

        self.board = Board()

        self.board.pieces = {}
        self.assertTrue(self.board.is_won())

        self.board.pieces = {Piece(0, None, True)}
        self.assertTrue(self.board.is_won())

        self.board.pieces = {Piece(1, None, True)}
        self.assertTrue(self.board.is_won())

        self.board.pieces = {Piece(0, None, True), Piece(1, None, True)}
        self.assertFalse(self.board.is_won())

    def test_is_possible_move(self):
        tiger = Card("tiger", [(-2, 0), (1, 0)])
        elephant = Card("elephant", [(-1, -1), (-1, 1), (0, -1), (0, 1)])
        crane = Card("crane", [(-1, 0), (1, -1), (1, 1)])

        #Valid moves
        self.assertTrue(self.board.is_possible_move(tiger, 0, [4, 2], [2, 2]))
        self.assertTrue(self.board.is_possible_move(tiger, 1, [0, 2], [2, 2]))
        self.assertTrue(self.board.is_possible_move(elephant, 0, [4, 4], [3, 3]))
        self.assertTrue(self.board.is_possible_move(elephant, 1, [0, 4], [1, 3]))
        self.assertTrue(self.board.is_possible_move(crane, 0, [4, 1], [3, 1]))
        self.assertTrue(self.board.is_possible_move(crane, 1, [0, 0], [1, 0]))

        #Invalid moves

        #correct start and player, invalid end for card
        self.assertFalse(self.board.is_possible_move(tiger, 0, [4, 2], [3, 2]))
        self.assertFalse(self.board.is_possible_move(tiger, 1, [0, 2], [4, 2]))

        #correct player, wrong start with a valid end(if the start were valid)
        self.assertFalse(self.board.is_possible_move(tiger, 0, [3, 1], [1, 1]))
        self.assertFalse(self.board.is_possible_move(tiger, 1, [1, 4], [2, 4]))

        #correct start and player, valid end but there is a friendly piece
        self.assertFalse(self.board.is_possible_move(elephant, 0, [4, 4], [4, 3]))
        self.assertFalse(self.board.is_possible_move(elephant, 1, [0, 3], [0, 2]))

        # correct start and player, valid end but its not on the board
        self.assertFalse(self.board.is_possible_move(crane, 0, [4, 4], [5, 3]))
        self.assertFalse(self.board.is_possible_move(crane, 1, [0, 2], [-1, 1]))

    def test_move_piece(self):

        self.assertFalse(type(self.board.board_state[1][2]) == Piece)
        self.assertFalse(self.board.board_state[1][2])
        self.board.move_piece([0, 2], [1, 2])
        self.assertTrue(type(self.board.board_state[1][2]) == Piece)
        self.assertFalse(self.board.board_state[0][2])

        self.assertEqual(self.board.board_state[1][2].location, [1, 2])

        self.assertEqual(len(self.board.pieces), 10)
        self.board.move_piece([0, 1], [4, 1])
        self.board.move_piece([4, 1], [4, 0])
        self.board.move_piece([4, 0], [4, 4])
        self.board.move_piece([4, 4], [4, 3])
        self.assertEqual(len(self.board.pieces), 6)
        self.assertFalse(self.board.board_state[4][0])
        self.assertFalse(self.board.board_state[4][1])
        self.assertFalse(self.board.board_state[4][4])

        self.assertEqual(self.board.board_state[4][3].location, [4, 3])


    def test_remove_piece(self):
        self.assertEqual(len(self.board.pieces), 10)
        self.board.remove_piece(1, 2)
        self.assertEqual(len(self.board.pieces), 10)
        self.board.remove_piece(0, 0)
        self.assertEqual(len(self.board.pieces), 9)