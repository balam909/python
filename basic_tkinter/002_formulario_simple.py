#! /usr/bin/python
# -*- coding: utf-8 -*-

import sys
from tkinter import *

def onClickOk():
	try:
		value=int(inputText.get())
		value*=5
		etiqueta.config(text=value)
	except ValueError as e:
		etiqueta.config("Introduce un numero")

app=Tk()
app.title("Mi segunda app Grafica")

vp=Frame(app)
vp.grid(column=0,row=0,padx=50,pady=10)
vp.columnconfigure(0,weight=1)
vp.rowconfigure(0,weight=1)

etiqueta=Label(vp,text="Valor")
etiqueta.grid(column=2,row=2,sticky=(W,E))

button=Button(vp,text="OK!", command=onClickOk)
button.grid(column=1,row=1)

valor=""
inputText=Entry(vp,width=10,textvariable=valor)
inputText.grid(column=2,row=1)

app.mainloop()
