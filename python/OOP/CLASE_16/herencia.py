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
        return f"\n[+] El gato {self.nombre} hace ¡Miau!\n"

class Perro(Animal):
    
    def hablar(self):
        return f"\n[+] El perro {self.nombre} hace ¡Guau!\n"
    
class Vaca(Animal):
    
    pass

gato = Gato("Juanito")
perro = Perro("Pedro")
vaca = Vaca("Lola")

print(gato.hablar())
print(perro.hablar())
print(vaca.hablar()) # La clase Vaca no tiene implementado el método hablar, por lo que se lanza una excepción NotImplementedError

