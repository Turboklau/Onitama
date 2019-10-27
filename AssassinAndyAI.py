import math
from OkitamaForRobots import Piece
from OkitamaForRobots import Game


"""There are several ways to motivate the AI:
1: Minimum distance between its own pieces and enemy pieces << This is easy but not really a win condition
2: Minimum distance between its own pieces and enemy master << Assassin Andy
3: Minimum distance between its own master and enemy shrine << Suicide Sam
4: Maximum distance between its own master and enemy pieces
5: Maximum distance between its own shrine and enemy master << This is hard to do with a depth of 1
6: Maximum difference in number of pieces
7: Being in the winning state (i.e. if there is a move that wins, take it)
"""

class AssassinAndyAI:

    def __init__(self, game, color):
        self.game = game
        self.color = color

    def decide_move(self):
        moves = self.game.move_list()
        for move in moves:
            move.points = self.evaluate_points(move)
        best_move = min(moves, key=lambda x: x.points)
        print()
        print()
        print(self.color)
        print(best_move.card.name)
        self.game.print_board(best_move.new_board_state)
        print(best_move.points)
        return best_move

    def evaluate_points(self, move):
        pieces = []
        enemy_master = None
        for piece in self.game.pieces:
            if piece.color == self.color:
                pieces.append(piece)
            elif piece.color != self.color and piece.type == "master":
                enemy_master = piece
        return self.total_distance_from_master(pieces, enemy_master, move.new_board_state)

    def total_distance_from_master(self, pieces, enemy_master, new_board_state):
        total_distance = 0
        master_location = self.game.get_piece_position_on_board(new_board_state, enemy_master)
        if not master_location:
            return 0
        for piece in pieces:
            piece_location = self.game.get_piece_position_on_board(new_board_state, piece)
            if piece_location:
                total_distance += self.distance_between_locations(piece_location, master_location)
        return total_distance


    def distance_between_locations(self, a, b):
        return math.sqrt((a[0]-b[0])**2 + (a[1]-b[1])**2)



def main():
    game = Game()
    game.set_up()
    game.process_input("1")

    andy1 = AssassinAndyAI(game, 'red')
    andy2 = AssassinAndyAI(game, 'blue')

    if game.current_player == 'red':
        andys = [andy1, andy2]
    else:
        andys = [andy2, andy1]

    while not game.is_won():
        for andy in andys:
            if not game.is_won():
                move = andy.decide_move()
                if move:
                    game.process_move(move.card.name, move.move_index, move.piece.id)
                else:
                    for card in game.cards:
                        if card.holder == andy.color:
                            game.process_swap(card)
                            break

                game.end_turn()
    print("winner is "+ game.current_player)

main()

