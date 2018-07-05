import random,tkinter,math

from Mine_Button import Mine_Button

class Board:
	width = 10
	height = 10
	board = None
	ui = None
	# ui_buttons = None

	def __init__(self):
		self.ui = tkinter.Tk()
		self.board = [[Mine_Button(self.ui) for j in range(self.width)] for i in range(self.height)]
		# self.ui_buttons = [[0 for j in range(self.width)] for i in range(self.height)]

	def drop_mines(self):
		for r_key,row in enumerate(self.board):
			for c_key,cell in enumerate(row):
				if random.random() % 10 > 0.9:
					self.board[r_key][c_key].val = "M"

	def place_count(self):
		for r_key,row in enumerate(self.board):
			for c_key,cell in enumerate(row):
				# self.print(highlight=True,special_coords={"c":c_key,"r":r_key})
				if cell.val != "M":
					self.board[r_key][c_key].val = self.count_neighbors(r_key,c_key)

	def count_neighbors(self,r_key,c_key):
		count = 0

		count += self.has_mine_relative(r_key -1,c_key -1)
		count += self.has_mine_relative(r_key -1,c_key)
		count += self.has_mine_relative(r_key -1,c_key +1)

		count += self.has_mine_relative(r_key,c_key -1)
		count += self.has_mine_relative(r_key,c_key +1)

		count += self.has_mine_relative(r_key +1,c_key -1)
		count += self.has_mine_relative(r_key +1,c_key)
		count += self.has_mine_relative(r_key +1,c_key +1)

		return count

	def has_mine_relative(self,r,c):
		if r < 0 or c < 0:
			return 0
		if c > self.width -1 or r > self.height -1:
			return 0
		if self.board[r][c].val == "M":
			return 1
		else:
			return 0

	def click(self,r,c):
		self.board[r][c]["text"] = self.board[r][c].val

	def print(self):
		for r_key,row in enumerate(self.board):
			for c_key,cell in enumerate(row):
				self.board[r_key][c_key]["text"] = " "

				self.board[r_key][c_key].grid(
					row=r_key,
					column=c_key%self.width)

				self.board[r_key][c_key]["command"] = lambda r_key=r_key,c_key=c_key: self.click(r_key,c_key)

		self.ui.mainloop()