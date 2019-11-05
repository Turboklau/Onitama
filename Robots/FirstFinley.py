class FirstFinley:

    def decide_move(self, board, me, robotinfo):
        """First Finley always takes the first legal move he can find"""

        # Inverts movement matrix if playing for opposing side
        mult = 1
        if me == 1:
            mult = -1

        my_hand = robotinfo.get_hand(me)

        # For every move
        for card in my_hand:
            for move in card.moves:

                # For every piece of mine
                for piece in board.pieces:
                    if piece.player == me:

                        # Is that move possible? If so, take it
                        start = piece.location
                        end = [start[0] + mult * move[0],
                               start[1] + mult * move[1]]

                        if board.is_possible_move(card, me, start, end):
                            print("Player " + str(me + 1) + ": " + card.name)
                            return card, piece.location, end

        print("No available moves (I'm probably lying)")