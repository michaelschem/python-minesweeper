import tkinter

class Mine_Button(tkinter.Button):
	val = None

	def __init__(self,ui):
		tkinter.Button.__init__(self,ui)