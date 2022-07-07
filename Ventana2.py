# -*- coding: utf-8 -*-
"""
Created on Tue Jul  5 15:40:42 2022

@author: jduquegi
"""

from tkinter import *
win=Tk()
win.title("Ventana 2")
win.geometry("300x200")
def imprimir():
    a = int(input("Ingrese la variable a:"))
    b = int(input("Ingrese la variable b:"))
    c = a+b
    print("La suma de a y b es:", c)
    
but1=Button(win,text="Imprimir", fg="blue", command=imprimir)
but2=Button(win, text="Salir", fg="red", command = win.quit)
but1.pack()
but2.pack()
win.mainloop()

