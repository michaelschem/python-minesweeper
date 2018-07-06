import random,tkinter,threading,math

from Mine_Button import Mine_Button

class Board:
	width = 36
	height = 16
	total_mines = 99
	board = None
	ui = None
	neighbors = [[-1,-1],[-1,0],[-1,1],[0,-1],[0,1],[1,-1],[1,0],[1,1]]

	def __init__(self):
		self.ui = tkinter.Tk()
		self.board = [[Mine_Button(self.ui) for j in range(self.width)] for i in range(self.height)]
		# self.ui_buttons = [[0 for j in range(self.width)] for i in range(self.height)]

	def drop_mines(self):
		while self.total_mines > 0:
			self.board[math.floor((random.random() * 10) % self.height)][math.floor((random.random() * 10) % self.width)].val = "M"
			self.total_mines -= 1

	def place_count(self):
		for r_key,row in enumerate(self.board):
			for c_key,cell in enumerate(row):
				# self.print(highlight=True,special_coords={"c":c_key,"r":r_key})
				if cell.val != "M":
					self.board[r_key][c_key].val = self.count_neighbors(r_key,c_key)

	def count_neighbors(self, r_key, c_key):
		count = 0

		for i in self.neighbors:
			if self.safe_check("M", r_key + i[0], c_key + i[1]):
				count += 1

		return count

	def expand_zeros(self):
		for r_key,row in enumerate(self.board):
			for c_key,cell in enumerate(row):
				if not cell.hidden:
					for i in self.neighbors:
						if self.safe_check(0, r_key + i[0], c_key + i[1]) and self.board[r_key + i[0]][c_key + i[1]].hidden:
							self.board[r_key + i[0]][c_key + i[1]].show()
							self.expand_zeros()

	def expand_frindge(self):
		positions_to_check = []
		for r_key,row in enumerate(self.board):
			for c_key,cell in enumerate(row):
				if not cell.hidden and not cell.locked:
					positions_to_check.append({"r":r_key,"c":c_key})

		for position in positions_to_check:
			for i in self.neighbors:
				if position["r"] + i[0] < self.height and position["c"] + i[1] < self.width and position["r"] + i[0] != -1 and position["c"] + i[1] != -1:
					self.board[position["r"] + i[0]][position["c"] + i[1]].show()
					self.board[position["r"] + i[0]][position["c"] + i[1]].locked = True

	def safe_check(self, type, r, c):
		if r < 0 or c < 0:
			return False
		if c > self.width -1 or r > self.height -1:
			return False
		if self.board[r][c].val == type:
			return True
		else:
			return False

	def click(self, r, c):
		self.board[r][c].show()
		if self.board[r][c].val == 0:
			self.expand_zeros()
			self.expand_frindge()

		# self.board[r][c]["highlightbackground"] = "#8EF0F7",

	def display(self):
		for r_key,row in enumerate(self.board):
			for c_key,cell in enumerate(row):
				self.board[r_key][c_key]["text"] = self.board[r_key][c_key].val

				# tkinter.ttk.Style().configure('green/black.TButton', foreground='green', background='black')

				self.board[r_key][c_key]["command"] = lambda r_key=r_key, c_key=c_key: self.click(r_key, c_key)

				# self.board[r_key][c_key]["style"]='green/black.TButton'

				self.board[r_key][c_key].grid(
					row=r_key,
					column=c_key % self.width)


		UI_Thread = threading.Thread(target=self.ui.mainloop())
		UI_Thread.start()
