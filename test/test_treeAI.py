from unittest import TestCase

from Game import Game
from Robotinfo import Robotinfo
from Robots import DirectDerek
from Robots import TreeAI

class TestTreeAI(TestCase):
    def test_decide_move(self):
        self.fail()

    def test_get_new_board_states(self):
        treeAI = TreeAI(1)
        game = Game(treeAI, DirectDerek)
        robotinfo = Robotinfo(game)
        board = robotinfo.get_board_class()
        me = robotinfo.get_me()
        me_hand = robotinfo.get_hand(me)
        mid_card = robotinfo.get_mid_card()

        print(me_hand)
        self.assertTrue(True)


    def test_dirty_swap(self):
        self.fail()

    def test_minimax(self):
        self.fail()

    def test_evaluate_points(self):
        self.fail()
