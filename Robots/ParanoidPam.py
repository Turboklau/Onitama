import random
from Robots.BaseAI import BaseAI

"""Pam kills and avoids being killed."""

class ParanoidPam(BaseAI):
	def __init__(self, enraged=False):
		super().__init__()
		self.enraged = enraged

	def evaluate_points(self, board, me, robotinfo):
		mod = random.uniform(0,1)
		for piece in board.pieces:
			if piece.player == me:
				if self.in_danger(board, piece.location, robotinfo, me):
					mod += 1
		if self.enraged:
			return -len(board.pieces)*100 - mod
		return -len(board.pieces) - mod*100


	def in_danger(self, board, location, robotinfo, me):

		flip = -1
		if me == 1:
			flip = 1

		for enemy_piece in board.pieces:
			if enemy_piece.player != me:
				x, y = enemy_piece.location
				for card in robotinfo.get_hand(1-me):
					for move in card.moves:
						#print([move[0]*flip+x, move[1]*flip+y] == location)
						if [move[0]+x*flip, move[1]+y*flip] == location:
							print("as")
							return True

	def n_dangers(self, board, location, robotinfo, me):
		n_dangers = 0
		flip = 1

		for enemy_piece in board.pieces:
			if enemy_piece.player != me:
				x, y = enemy_piece.location
				for card in robotinfo.get_hand(1-me):
					for move in card.moves:
						if [move[0]+x*flip, move[1]+y*flip] == location:
							n_dangers += 1
		return n_dangers


