class Player:
    def __init__(self, strategy, hand=[], score=0):
        self.strategy = strategy
        self.hand = hand
        self.score = score

    def get_move(self, board, player, players, mid_card):
        return self.strategy.decide_move(board, player, players, mid_card)