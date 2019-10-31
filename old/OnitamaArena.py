from OnitamaForRobots import Game
from Robots.AssassinAndyAI import AssassinAndyAI
from Robots.DirectDerek import DirectDerek
from Robots.ErraticErin import ErraticErin
from Robots.RandomRebecca import RandomRebecca
from Robots.TacticalTanya import TacticalTanya


def pvp_loop(game):
    print("Starting player is " + game.current_player)
    while not game.is_won():
        print("Next turn: " + game.current_player)
        human_turn(game, True)

def pve_loop(robot, game):
    print()
    print("You are blue")
    while not game.is_won():
        if robot.color == game.current_player:
            robot_turn(robot, game)
        #player turn
        human_turn(game, False)

        print("Next turn: " + game.current_player)

        # robot turn
        robot_turn(robot, game)



def robot_battle_loop(robot1, robot2, game):
    if game.current_player == 'red':
        robots = [robot1, robot2]
    else:
        robots = [robot2, robot1]
    while not game.is_won():
        for robot in robots:
            if not game.is_won():
                robot_turn(robot, game)

def robot_turn(robot, game):
    move = robot.decide_move(game)
    if move:
        game.process_move(move.card.name, move.move_index, move.piece.id)
    else:
        for card in game.cards:
            if card.holder == robot.color:
                game.process_swap(card)
                break

    game.end_turn()

def human_turn(game, print_board):
    print("Next turn: " + game.current_player)
    if len(game.move_list()) < 1:
        swap_done = False
        while not swap_done:
            print("You have no possible moves.")
            swap = input("Enter the name of the card you want to swap with the middle: ")
            swap_done = game.process_swap(swap)
    else:
        game.process_input("1")
        if print_board:
            game.process_input("2")
        game.process_input("3")
        move = False
        while not move:
            print()
            name = input("Enter the name of the card to use: ")
            index = input("Enter the move index of the move to use: ")
            piece_id = input("Enter the piece id: ")
            move = game.process_move(name, index, piece_id)
    game.end_turn()

def get_robot(name, color):
    if name == "andy":
        return AssassinAndyAI(color)
    elif name == 'derek':
        return DirectDerek(color)
    elif name == 'rebecca':
        return RandomRebecca(color)
    elif name == 'erin':
        return ErraticErin(color)
    elif name == 'tanya':
        return TacticalTanya(color, 3)


def print_options():
    print()
    print("1: Player VS Player")
    print("2: Player VS AI")
    print("3: AI VS AI")
    print()

def main():
    game = Game()
    print()
    print("Welcome to Onitama! This is a 2 player game similar to chess.")
    print_options()
    mode = input("Please choose a mode: ")
    while mode != "1" and mode != "2" and mode != "3":
        print("DOES NOT COMPUTE. ENTER 1, 2 or 3.")
        print_options()
        mode = input("Please choose a mode: ")
    game.set_up()
    if mode == "1":
        pvp_loop(game)
    elif mode == "2":
        robot1 = get_robot('erin', 'red')
        pve_loop(robot1, game)
    elif mode == "3":
        robot1 = get_robot('tanya', 'red')
        robot2 = get_robot('derek', 'blue')
        robot_battle_loop(robot1, robot2, game)
    print("winner is " + game.current_player)

main()