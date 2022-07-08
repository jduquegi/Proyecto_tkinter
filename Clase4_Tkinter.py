# -*- coding: utf-8 -*-
"""
Created on Thu Jul  7 16:46:20 2022
Desarrollado por: Javier Andrés Duque Giraldo
CC: 1225089534
EDEQ 

Éste es un módulo de aprendizaje para probar los campos de texto (Entry)
"""

from tkinter import *

root=Tk()
root.title("Entrada")
root.geometry("400x300")

nombre = StringVar()
apellido = StringVar()

nombre.set("Escribe aquí tu nombre")
apellido.set("Escribe aquí tu apellido")

def saludar():
    saludo_nombre=("Hola :" + nombre.get() + " " + apellido.get())
    etiqueta_saludo = Label(root, text=saludo_nombre)
    etiqueta_saludo.place(x=10, y=130)
    
    
etiqueta1 = Label(root, text="Escribe aquí tu nombre: ")
etiqueta1.place(x=10, y=10)

entrada1 = Entry(root, textvariable=nombre)
entrada1.place(x=170, y=10)

etiqueta2 = Label(root, text="Escribe aquí tu apellido: ")
etiqueta2.place(x=10, y=40)

entrada2 = Entry(root, textvariable=apellido)
entrada2.place(x=170, y=40)

boton = Button(root, text="Saludar ahora", command=saludar)
boton.place(x=10, y=100)




root.mainloop()





