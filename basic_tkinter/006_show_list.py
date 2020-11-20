#!/usr/bin/python
# -*- coding: utf-8 -*-

from tkinter import *

def onClickDraw():
	plist=['Name1','Name2','Name3']
	for item in plist:
		listBox.insert(END,item)

root=Tk()
listBox=Listbox(root)
button=Button(root,text='Draw List',command=onClickDraw)
button.pack()
listBox.pack()
root.mainloop()
