#!/usr/bin/env python3

def mi_decorador(funcion):
    def wrapper():
        print("Antes de la función")
        funcion()
        print("Después de la función")
    return wrapper

@mi_decorador
def saludo():
    print("Hola Mundo")
    
# saludo()

'''
+---------------------------------------------------------------------+
'''

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def __str__(self):
        return f"Nombre: {self.nombre}, Edad: {self.edad}"
    
    @property
    def edad(self): # Getter
        return self._edad
    
    @edad.setter
    def edad(self, edad): # Setter
        if edad <= 0:
            raise ValueError("[!] La edad no puede ser negativa o cero")
        self._edad = edad
    

# p = Persona("Juan", 30)
# print(p)

# p.edad = -40
# print(p)

'''
+---------------------------------------------------------------------+
'''

import time

def cronometro(funcion):
    def wrapper():
        inicio = time.time()
        funcion()
        fin = time.time()
        print(f"La función {funcion.__name__} tardó {fin - inicio} segundos")
    return wrapper

@cronometro
def pausa_corta():
    time.sleep(1)

@cronometro
def pausa_larga():
    time.sleep(2)
    
# pausa_corta()
# pausa_larga()

# cronometro(pausa_corta)()

'''
+---------------------------------------------------------------------+
'''

# *args

def suma(*args):
    return sum(args)

print(suma(1, 2, 3, 4, 5))

# **kwargs

def diccionario(**kwargs):
    return kwargs

print(diccionario(a=1, b=2, c=3))
    
# *args y **kwargs

def funcion(*args, **kwargs):
    print(args)
    print(kwargs)
    
funcion(1, 2, 3, a=4, b=5, c=6)

