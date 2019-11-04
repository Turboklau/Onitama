
from Robots.BaseAI import BaseAI

"""Sadistic Sarah kills mercilessly, but keeps her distance"""
"""She lies in the shadows waiting for opponent to take their move before she strikes"""


class SadisticSarah(BaseAI):

	def evaluate_points(self, board, me):
		mod = 0
		for piece in board.pieces:
			if piece.player == me:
				x, y = piece.location
				for i in [-1,0,1]:
					for j in [-1,0,1]:
						legal = range(5)
						if i+x in legal and j+y in legal:
							if board.board_state[i+x][j+y] in board.pieces:
								if board.board_state[i+x][j+y].player == 1-me:
									mod += 5

		return -len(board.pieces) - mod


	def in_danger(self, board, piece):

		me = piece.player

		for enemy_piece in board.pieces:
			if enemy_piece.player != me:
				x, y = piece.location
				for card in 