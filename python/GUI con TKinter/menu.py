#!/usr/bin/env python3

import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog

def accion_menu():
    messagebox.showinfo("MENU EXTRA", "PWNED!")
    
def abrir():
    ruta_archivo = tk.filedialog.askopenfilename(title="Abrir archivo")
    print(ruta_archivo)

root = tk.Tk() # Crear una ventana raíz de la aplicación
root.title("MENU") # Título de la ventana
root.geometry("400x400") # Dimensiones de la ventana

BARRA_MENU = tk.Menu(root) # Crear una barra de menú

root.config(menu=BARRA_MENU) # Configurar la barra de menú

menu1 = tk.Menu(BARRA_MENU, tearoff=0) # Crear un menú
menu2 = tk.Menu(BARRA_MENU, tearoff=0) # Crear un menú
menu3 = tk.Menu(BARRA_MENU,  tearoff=0) # Crear un menú
menu4 = tk.Menu(BARRA_MENU,  tearoff=0) # Crear un menú

menu1.add_command(label="Nuevo") # Añadir una opción al menú
menu1.add_command(label="Abrir", command=abrir) # Añadir una opción al menú
menu1.add_command(label="Guardar")

menu2.add_command(label="Cortar") # A
menu2.add_command(label="Copiar")
menu2.add_command(label="Pegar")

menu3.add_command(label="Acerca de...") # Añadir una opción al menú
menu3.add_command(label="Ayuda")

menu4.add_command(label="EXTRAS", command=accion_menu) # Añadir una opción al menú


BARRA_MENU.add_cascade(label="Archivo", menu=menu1) # Añadir un menú a la barra de menú
BARRA_MENU.add_cascade(label="Editar", menu=menu2) # Añadir un menú a la barra de menú
BARRA_MENU.add_cascade(label="Ayuda", menu=menu3) # Añadir un menú a la barra de menú
BARRA_MENU.add_cascade(label="Extras", menu=menu4) # Añadir un menú a la barra de menú

root.mainloop() # Bucle principal de la ventana