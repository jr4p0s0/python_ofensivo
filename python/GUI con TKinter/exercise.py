#!/usr/bin/env python3

import tkinter as tk

def accion_del_boton():
    print("Botón presionado")
    root.quit()

def get_data():
    data = text_w.get("1.0", tk.END)
    print(f"\n [+] Datos introducidos por el usuario:\n\n {data}")

root = tk.Tk() # Crear una ventana raíz de la aplicación

root.title("Ventana de Ejercicio") # Título de la ventana

root.geometry("400x400") # Tamaño de la ventana

text_w = tk.Text(root, width=30, height=10) # Campo de texto
text_w.pack(pady=15, padx=50) # Campo de texto

label = tk.Label(root, text="Mi primer label", bg="Blue") # Título de la ventana
label2 = tk.Label(root, text="Mi segundo label", bg="Red") # Título de la ventana
label3 = tk.Label(root, text="Mi tercer label", bg="Green") # Título de la ventana

label.place(x=0, y=0) # Ubicar el label en la ventana
label3.place(x=0, y=20) # Ubicar el label en la ventana
label2.place(relx=0.40, rely=.40, anchor=tk.CENTER) # Ubicar el label en la ventana


button = tk.Button(root, text="Recoger datos de la entrada", command=get_data) # Botón para salir de la ventana

button.pack(pady=15, padx=50) # Ubicar el botón en la ventana

root.mainloop() # Bucle principal de la ventana

