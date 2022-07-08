# -*- coding: utf-8 -*-
"""
Created on Thu Jul  7 16:46:20 2022
Desarrollado por: Javier Andrés Duque Giraldo
CC: 1225089534
EDEQ 

Éste es un módulo de aprendizaje para probar los campos de texto (Entry), con 
diferentes aspectos y funciones.
"""

from tkinter import *

root=Tk()
root.title("Entrada")
root.geometry("400x300")
root.resizable(0,0)       #El usuario no podrá modificar el tamaño de la pantalla

nombre = StringVar()
apellido = StringVar()
saludo = StringVar()

# =============================================================================
# nombre.set("Escribe aquí tu nombre")
# apellido.set("Escribe aquí tu apellido")
# =============================================================================

def saludar():
    saludo.set("Hola :" + nombre.get() + " " + apellido.get())  
    
etiqueta1 = Label(root, text="Escribe aquí tu nombre: ", bd=4, bg="red", font=
                  "curier 10")
etiqueta1.place(x=10, y=10)

entrada1 = Entry(root, textvariable=nombre, bd=5)
entrada1.place(x=170, y=10)

etiqueta2 = Label(root, text="Escribe aquí tu apellido: ", bd=4, bg="red", 
                  font="curier 10")
etiqueta2.place(x=10, y=40)

entrada2 = Entry(root, textvariable=apellido, bd=5)
entrada2.place(x=170, y=40)

boton = Button(root, text="Saludar ahora", command=saludar, bd=5, bg="red")
boton.place(x=10, y=100)

entrada3 = Entry(root, bd=20, font=("Curier 10"), textvariable=saludo, state
                 ="disable")
entrada3.place(x=10, y=160)

root.mainloop()

## bd --> Especifica el tamaño del borde
## bg --> Especifica el color del boton
## font --> Especifica el tipo y tamaño de la letra
## state="disable" --> Especifica que el Empty no pueda editarse



