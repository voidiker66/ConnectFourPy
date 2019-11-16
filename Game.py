
class Game():
	def __init__(self):
		self.board = self.init_board()
		self.turn = 0

	# initialize a 7x6 board of zeros
	def init_board(self):
		return [[0 for x in range(6)] for x in range(7)]

	# places a token at the specified column
	# token populates the highest "empty" row
	def place_token(self, column):
		row = 0
		while self.board[column][5 - row] == 0:
			if row >= 5:
				# invalid column
				return False
			row = row + 1

		# if a valid move, place token, increment turn count, and return successful
		self.board[column][row] = (self.turn % 2) + 1
		self.turn = self.turn + 1
		return True