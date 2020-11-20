#!/usr/bin/python
# -*- coding: utf-8 -*-

from tkinter import *

root = Tk()
li = 'Diego Matias Martin Carla Lorena Roberto'.split()
movie = ['El padrino', 'Naruto', 'La gran estafa', 'Los juegos del hambre']
listb = Listbox(root)
for item in li :
	listb.insert(0,item)

listb.pack()
root.mainloop()
