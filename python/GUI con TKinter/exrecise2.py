#!/usr/bin/env python3

import tkinter as tk

root = tk.Tk() # Crear una ventana raíz de la aplicación

root.title("Ventana de Ejercicio") # Título de la ventana

frame = tk.Frame(root, bg="blue", width=200, height=200, bd=8) # Crear un frame
frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER) # Ubicar el frame en la ventana

label1 = tk.Label(frame, text="buenas tardes", bg="RED") # Título de la ventana

label1.pack(pady=15, padx=50) # Ubicar el label en la ventana

root.mainloop() # Bucle principal de la ventana