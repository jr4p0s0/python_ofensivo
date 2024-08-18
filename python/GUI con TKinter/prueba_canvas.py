#!/usr/bin/env python3

import tkinter as tk

root = tk.Tk() # Crear una ventana raíz de la aplicación

root.title("Ventana de Ejercicio") # Título de la ventana

canvas = tk.Canvas(root, width=400, height=400, bg="blue") # Crear un canvas
oval = canvas.create_oval(100, 100, 300, 300, fill="red") # Crear un óvalo
rect = canvas.create_rectangle(50, 50, 100, 350, fill="green") # Crear un rectángulo
line = canvas.create_line(0, 0, 400, 400, fill="white") # Crear una línea

canvas.pack(pady=25) # Ubicar el canvas en la ventana


root.mainloop() # Bucle principal de la ventana