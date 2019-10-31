class Piece:
    def __init__(self, player, location=None, master=False):
        self.master = master
        self.player = player
        self.location = location

        assert type(self.player) == int