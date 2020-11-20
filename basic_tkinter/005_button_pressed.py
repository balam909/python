#!/usr/bin/python
# -*- coding: utf-8 -*-

from tkinter import *

def onClickButton():
	label=Label(root, text='Usted presiono \nel boton')
	label.pack()
	#button['bg']='blue'
	#button['fg']='white'
	button['highlightbackground']='blue'

root=Tk()
root.geometry('100x110+350+70')
button=Button(root, text='Presionar', command=onClickButton)
button.pack()
root.mainloop()
