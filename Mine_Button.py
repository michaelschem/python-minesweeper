import tkinter


class Mine_Button(tkinter.Button):
	val = None
	hidden = None
	locked = None

	def __init__(self,ui):
		tkinter.Button.__init__(self,ui)
		self.hidden = True
		locked = False

	def show(self):
		self["text"] = self.val
		self.hidden = False
		# self["highlightbackground"] = "#8EF0F7"
