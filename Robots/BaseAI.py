"""There are several ways to motivate the AI:
1: Minimum distance between its own pieces and enemy pieces << This is easy but not really a win condition
2: Minimum distance between its own pieces and enemy master << Assassin Andy
3: Minimum distance between its own master and enemy shrine << Suicide Sam
4: Maximum distance between its own master and enemy pieces
5: Maximum distance between its own shrine and enemy master << This is hard to do with a depth of 1
6: Maximum difference in number of pieces
7: Being in the winning state (i.e. if there is a move that wins, take it)
"""

class BaseAI():

    def __init__(self, game, color):
        self.game = game
        self.color = color

    def decide_move(self):
        moves = self.game.move_list()
        for move in moves:
            move.points = self.evaluate_points(move)
        best_state = max(moves, key=lambda x: x.points)
        print()
        print()
        print(self.color)
        print(best_state.card.name)
        self.game.print_board(best_state.game_state.board_state)
        print(best_state.points)
        return best_state

    def evaluate_points(self, move):
        pass