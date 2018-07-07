import tkinter


class Mine_Button(tkinter.Button):
	val = None
	shown = None
	locked = None

	def __init__(self,ui):
		tkinter.Button.__init__(self,ui)
		self.shown = False
		locked = False

	def show(self):
		self["text"] = self.val
		self.shown = True
		self["highlightbackground"] = "#8EF0F7"
