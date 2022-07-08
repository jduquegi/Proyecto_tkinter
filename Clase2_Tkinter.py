# -*- coding: utf-8 -*-
"""
Desarrollado por: Javier Andrés Duque Giraldo
CC: 1225089534
Fecha: 7/07/2022
EDEQ 

Éste es un módulo de aprendizaje para crear botones con Tkinter (Forma 2)
"""
from tkinter import *
import tkinter as tk
from tkinter import ttk

root = tk.Tk()

def seleccionar(opcion):
    label_opcion = Label(root, text = opcion)
    label_opcion.pack()
    
ttk.Button(root, text="Python", command=lambda: seleccionar("Python")).pack()

ttk.Button(root, text="Java", command=lambda: seleccionar("Java")).pack()

ttk.Button(root, text="Javascript", command=lambda: seleccionar("Javascript")).pack()

root.mainloop()