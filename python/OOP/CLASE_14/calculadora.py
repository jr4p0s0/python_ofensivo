#!/usr/bin/env python3

class Calculadora:
    
    @staticmethod
    def suma(a, b):
        return a + b
    
    @staticmethod
    def resta(a, b):
        return a - b
    
    @staticmethod
    def multiplicacion(a, b):
        return a * b
    
    @staticmethod
    def dividir(a, b):
        return a / b if b != 0 else "No se puede dividir por cero"
    

print(Calculadora.suma(2, 3))
print(Calculadora.resta(2, 3))
print(Calculadora.multiplicacion(2, 3))
print(Calculadora.dividir(2, 3))
print(Calculadora.dividir(2, 0))
