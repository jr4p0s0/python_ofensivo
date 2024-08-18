#!/usr/bin/env python3

'''
    El concepto de encapsulamiento en programación orientada a objetos es la capacidad de una clase de ocultar los atributos y métodos de una clase.
    En Python, el encapsulamiento se logra utilizando el guión bajo como prefijo en los atributos y métodos de una clase.

    _ : Atributos y métodos protegidos
    __ : Atributos y métodos privados
    
    La diferencia entre los atributos y métodos protegidos y privados es que los atributos y métodos protegidos pueden ser accedidos desde una subclase,
    mientras que los atributos y métodos privados no pueden ser accedidos desde una subclase.

'''

class Ejemplo:
    
    def __init__(self):
        self.__atributo_privado = "Soy un atributo privado"
        self._atributo_protegido = "Soy un atributo protegido"
        self.atributo_publico = "Soy un atributo público"

    def __metodo_privado(self):
        return "Soy un método privado"
    
    def _metodo_protegido(self):
        return "Soy un método protegido"
    
    def metodo_publico(self):
        return "Soy un método público"
    
ejemplo = Ejemplo()

'''
+----------------------------------------------------------------------------------------------------+
'''

class Contador:
    
    def __init__(self, limite):
        
        self.limite = limite
    
    def __iter__(self):
        
        self.contador = 0 # Inicializamos el contador
        
        return self
    
    def __next__(self):
        
        if self.contador < self.limite: # Si el contador es menor que el límite
            self.contador += 1          # Incrementamos el contador
            return self.contador        # Retornamos el contador
        else:
            raise StopIteration

contador = Contador(15)

for numero in contador:
    print(numero)
    
