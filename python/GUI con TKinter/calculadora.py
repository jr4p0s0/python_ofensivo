#!/usr/bin/env python3

import tkinter as tk
from tkinter import messagebox, filedialog

class Calculadora:
    
    def __init__(self, master):
        self.master = master
        self.master.title("Calculadora")
        # self.master.geometry("400x400")
        
        # non editable by user entry widget --> tk.Entry(state="disabled")
        
        self.display = tk.Entry(master, font=("Arial", 25), justify="right", width=16, bd=10, insertwidth=1, bg="powder blue")
        self.display.grid(row=0, column=0, columnspan=4)
        
        row = 1
        col = 0 
        
        buttons = [
            "7", "8", "9", "/",
            "4", "5", "6", "*",
            "1", "2", "3", "-",
            "C", "0", ".", "+", 
            "="
        ]
        
        for button in buttons:
            self.build_button(button, row, col)
            col += 1 
            if col > 3:
                col = 0 
                row += 1
        
        self.master.bind("<Key>", self.key_pressed)

    def key_pressed(self, event):
        if event.char in "0123456789.+-*/":
            self.click(event.char)
        elif event.keysym == "Return":
            self.calculate()
        elif event.keysym == "Escape":
            self.clear_display()
        elif event.keysym == "BackSpace":
            self.display.delete(len(self.display.get()) - 1, tk.END)
    
    def build_button(self, button, row, col):
        if button == "C":
            b = tk.Button(self.master, text=button, font=("Arial", 15), width=5, height=2, command=self.clear_display)
        elif button == "=":
            b = tk.Button(self.master, text=button, font=("Arial", 15), width=5, height=2, command=self.calculate)
        else:
            b = tk.Button(self.master, text=button, font=("Arial", 15), width=5, height=2, command=lambda: self.click(button))
        b.grid(row=row, column=col)
    
    def click(self, text):
        self.display.insert(tk.END, text)
    
    def clear_display(self):
        self.display.delete(0, tk.END)
        
    def calculate(self):
        try:
            result = eval(self.display.get())
            self.display.delete(0, tk.END)
            self.display.insert(tk.END, str(round(result, 8)))
        except:
            messagebox.showerror("Error", "Operación inválida")



root = tk.Tk()
gui = Calculadora(root)

# cambiar el color de fondo

root.configure(bg="dark gray")

root.mainloop()