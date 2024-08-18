#!/usr/bin/env python3

class Estudiantes:
    
    estudiantes = []
    
    @classmethod
    def crear_estudiante(cls, nombre, edad):
        if edad >= 22:
            return cls(nombre, edad)
        else:
            print(f"\n [!] No se puede crear el estudiante {nombre}, es menor de 22 años\n")
    
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        
        Estudiantes.estudiantes.append( self )
        
    @classmethod
    def mostrar_estudiantes(cls):
        for i, estudiante in enumerate(cls.estudiantes):
            print(f"\t [+] Estudiante numero [{i+1}]: {estudiante.nombre} - {estudiante.edad}")



Estudiantes.crear_estudiante("Juan", 20)
Estudiantes.crear_estudiante("Maria", 22)
Estudiantes.crear_estudiante("Pedro", 21)
Estudiantes.crear_estudiante("Ana", 23)
Estudiantes.crear_estudiante("Carlos", 24)

print("\n [+] Estudiantes creados:\n")

Estudiantes.mostrar_estudiantes()