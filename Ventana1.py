# -*- coding: utf-8 -*-
"""
Desarrollado por: Javier Andrés Duque Giraldo
CC: 1225089534
EDEQ 

Éste es un módulo de prueba para crear formularios inteligentes con tkinter y
Pandas
"""

from tkinter import *
win = Tk()
win.title("Mi primera ventana")
eti = Label(win, text="Hola humano")
but1 = Button(win,text="Minimizar",command=win.iconify)
eti.pack()
but1.pack()
win.geometry("300x200")
win.mainloop()

