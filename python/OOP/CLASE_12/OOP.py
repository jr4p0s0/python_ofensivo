#!/usr/bin/env python3

import pwn

class Persona:
    
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    def saludo(self):
        print(f"Hola, mi nombre es {self.nombre} y tengo {self.edad} años.")

marcelo = Persona("Marcelo", 25)

marcelo.saludo()

class CuentaBancaria:
        
        def __init__(self, titular, saldo):
            self.titular = titular
            self.saldo = saldo
        def depositar(self, cantidad):
            self.saldo += cantidad
            print(f"[+] Se han depositado {cantidad} en la cuenta de {self.titular}. El saldo actual es de {self.saldo}")
        def retirar(self, cantidad):
            if cantidad > self.saldo:
                print("[!] No se puede retirar esa cantidad, saldo insuficiente.")
            else:
                self.saldo -= cantidad
                print(f"[+] Se han retirado {cantidad} de la cuenta de {self.titular}. El saldo actual es de {self.saldo}")

cuenta1 = CuentaBancaria("Marcelo", 1000)

print(cuenta1.saldo)

cuenta1.depositar(500)

cuenta1.retirar(2000)