import tkinter


class Mine_Button(tkinter.Button):
	val = None
	hidden = None

	def __init__(self,ui):
		tkinter.Button.__init__(self,ui)
		self.hidden = True

	def show(self):
		self["text"] = self.val
		self.hidden = False
		self["highlightbackground"] = "#8EF0F7"
