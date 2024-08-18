#!/usr/bin/env python3

class Persona:
    
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
    def presentacion(self):
        print(f"\n[+] Hola, mi nombre es {self.nombre} y tengo {self.edad} años\n")


Jaime = Persona("Jaime", 22)
Jaime.presentacion()