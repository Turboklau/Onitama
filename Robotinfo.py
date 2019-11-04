import copy

class Robotinfo():
	def __init__(game):
		self.game = game

	def get_board_class():
		return copy.deep_copy(self.game.board)

	def get_board():
		return copy.deep_copy(self.game.board.board_state)

	def get_hand(player):
		return self.game.players[player].hand

	def get_midcard():
		return self.game.mid_card

	def get_cards():
		cards = []
		for player in self.game.players:
			cards += player.hand
		return cards + self.get_midcard()

	def in_hand(card, player):
		return card in self.get_hand(player)