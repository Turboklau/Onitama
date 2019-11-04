from Robotinfo import Robotinfo


class Player:
    def __init__(self, strategy, hand=[], score=0):
        self.strategy = strategy
        self.hand = hand
        self.score = score

    def get_move(self, game):
        robotInfo = Robotinfo(game)
        return self.strategy.decide_move(robotInfo)