# -*- coding: utf-8 -*-
"""
Created on Thu Jul  7 14:28:28 2022
Desarrollado por: Javier Andrés Duque Giraldo
CC: 1225089534
EDEQ 

Éste es un módulo de aprendizaje para crear botones con Tkinter (Forma 1)
"""

from tkinter import *
win=Tk()
win.title("Suma de valores enteros")
win.geometry("300x200")
def imprimir():
    label_a = Label(win, text = "Ingrese la variable a:")
    label_a.pack(side=LEFT)
    cuadro_a = Entry(win)
    cuadro_a.grid()
    
    label_b = Label(win, text = "Ingrese la variable b:")
    label_b.pack()
    cuadro_b = Entry(win)
    cuadro_b.grid()

    c = a+b
    
    label_c = Label(win, text = "La suma de a y b es:")
    label_c.pack()
    
but1=Button(win,text="Imprimir", fg="blue", command=imprimir, bg="black")
but2=Button(win, text="Salir", fg="red", command = win.quit)
but1.pack() # Posiciona el Botón en Pantalla
but2.pack()
win.mainloop()