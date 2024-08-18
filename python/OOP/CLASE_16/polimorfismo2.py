#!/usr/bin/env python3

class Automovil:
    
    def __init__(self, marca, modelo, tipo="Automovil"):
        self.marca = marca
        self.modelo = modelo
        self.tipo = tipo
        
    def describir(self):
        return f"\n[*] {self.tipo}: \n\t[+] Marca: {self.marca}\n\t[+] Modelo: {self.modelo}"
    
class Coche(Automovil):
    
    def __init__(self, marca, modelo):
        super().__init__(marca, modelo, tipo="Coche")
        
class Moto(Automovil):
        
    def __init__(self, marca, modelo):
        super().__init__(marca, modelo, tipo="Moto")
    
coche = Coche("Ford", "Fiesta")
moto = Moto("Yamaha", "FZ")

print(coche.describir())
print(moto.describir())