import random,tkinter,math

from Mine_Button import Mine_Button

class Board:
	width = 10
	height = 10
	board = None
	ui = None
	neighbors = [[-1,-1],[-1,1],[-1,0],[0,-1],[0,1],[1,-1],[1,0],[1,1]]

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

	def count_neighbors(self, r_key, c_key):
		count = 0

		for i in self.neighbors:
			count += self.has_relative("M",r_key + i[0],c_key + i[1])

		return count

	def expand_neighbors(self,r_key,c_key):
		for i in self.neighbors:
			if self.has_relative(0,r_key + i[0],c_key + i[1]) == 1:
				self.board[r_key + i[0]][c_key + i[1]]["text"] = 0
				self.expand_neighbors(r_key + i[0],c_key + i[1])

	def has_relative(self, type, r, c):
		if r < 0 or c < 0:
			return 0
		if c > self.width -1 or r > self.height -1:
			return 0
		if self.board[r][c].val == type:
			return 1
		else:
			return 0

	def click(self, r, c):
		self.board[r][c]["text"] = self.board[r][c].val
		if self.board[r][c].val == 0:
			self.expand_neighbors(r,c)
		# self.board[r][c]["highlightbackground"] = "#8EF0F7",

	def display(self):
		for r_key,row in enumerate(self.board):
			for c_key,cell in enumerate(row):
				self.board[r_key][c_key]["text"] = " "

				# tkinter.ttk.Style().configure('green/black.TButton', foreground='green', background='black')

				self.board[r_key][c_key]["command"] = lambda r_key=r_key, c_key=c_key: self.click(r_key, c_key)

				# self.board[r_key][c_key]["style"]='green/black.TButton'

				self.board[r_key][c_key].grid(
					row=r_key,
					column=c_key % self.width)



		self.ui.mainloop()