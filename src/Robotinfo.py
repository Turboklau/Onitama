import copy

class Robotinfo():
	def __init__(self, game):
		self.game = game

	def get_board_class(self):
		return copy.deepcopy(self.game.board)

	def get_board(self):
		return copy.deepcopy(self.game.board.board_state)

	def get_hand(self, player):
		return self.game.players[player].hand

	def get_midcardself(self):
		return self.game.mid_card

	def get_cards(self):
		cards = []
		for player in self.game.players:
			cards += player.hand
		return cards + self.get_midcard()

	def in_hand(self, card, player):
		return card in self.get_hand(player)