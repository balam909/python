#! /usr/bin/python
# -*- coding: utf-8 -*-

from tkinter import *

app=Tk()
app.title("Aplicaion grafica en python")
etiqueta=Label(app, text="Hola Mundo!!!")
button = Button(app, text="OK!!!")

etiqueta.pack()
button.pack()
app.mainloop()
