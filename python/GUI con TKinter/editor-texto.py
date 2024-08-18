#!/usr/bin/env python3

import tkinter as tk
from tkinter import messagebox, filedialog

class SimpleTextEditor:
    
    def __init__(self, root):
        self.root = root
        self.text_widget = tk.Text(root)
        self.text_widget.pack(expand=True, fill="both")
        self.current_file = None
    
    def open_file(self):
        file_path = filedialog.askopenfilename(title="Abrir archivo")
        if file_path:
            with open(file_path, "r") as file:
                self.text_widget.delete("1.0", tk.END)
                self.text_widget.insert("1.0", file.read())

            self.current_file = file_path

    def new_file(self):
        self.text_widget.delete("1.0", tk.END)
        self.current_file = None
    
    def save_file(self):
        if self.current_file:
            with open(self.current_file, "w") as file:
                file.write(self.text_widget.get("1.0", tk.END))
        else:
            self.save_file_as()

    def save_file_as(self):
        file_path = filedialog.asksaveasfilename(title="Guardar archivo")
        if file_path:
            with open(file_path, "w") as file:
                file.write(self.text_widget.get("1.0", tk.END))
            self.current_file = file_path

    def quit_confirm():
        if messagebox.askokcancel("Salir", "¿Estás seguro que deseas salir?"):
            root.quit()


root = tk.Tk()
root.geometry("800x800")

editor = SimpleTextEditor(root)

menu_bar = tk.Menu(root)
menu_options = tk.Menu(menu_bar, tearoff=0) # tearoff=0: No se puede separar el menú

menu_options.add_command(label="Nuevo", command=editor.new_file) # Opción de menú
menu_options.add_command(label="Abrir", command=editor.open_file) # Opción de menú
menu_options.add_command(label="Guardar", command=editor.save_file) # Opción de menú
menu_options.add_command(label="Guardar como...", command=editor.save_file_as) # Opción de menú
menu_options.add_separator() # Separador
menu_options.add_command(label="Salir", command=editor.quit_confirm) # Opción de menú

root.config(menu=menu_bar)
menu_bar.add_cascade(label="Archivo", menu=menu_options) # Menú con opciones: Nuevo, Abrir, Guardar, Separador, Salir

menu_bar.add_cascade(label="Editar") # Menú sin opciones
menu_bar.add_cascade(label="Ayuda") # Menú sin opciones


root.mainloop()
