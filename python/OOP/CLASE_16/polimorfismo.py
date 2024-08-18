#!/usr/bin/env python3

'''
    El concepto de herencia en programación orientada a objetos es la capacidad de una clase de heredar atributos y métodos de otra clase.
    En Python, la herencia se logra pasando la clase padre como argumento en la definición de la clase hija.
    
    En este ejemplo, la clase Estudiantes hereda de la clase Persona, por lo que la clase Estudiantes tiene acceso a los atributos y 
    métodos de la clase Persona.
'''

class Animal:
    
    def __init__(self, nombre):
        self.nombre = nombre
        
    def hablar(self):
        raise NotImplementedError("La Subclase debe implementar este método")

class Gato(Animal):
    
    def hablar(self):
        return f"¡Miau!\n"

class Perro(Animal):
    
    def hablar(self):
        return f"¡Guau!\n"
    
def hacer_hablar(animal):
    print(f"\n [+] {animal.nombre} dice: {animal.hablar()}")
    
gato = Gato("Juanito")
perro = Perro("Pedro")

hacer_hablar(gato)
hacer_hablar(perro)

