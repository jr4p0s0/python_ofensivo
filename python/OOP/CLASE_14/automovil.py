#!/usr/bin/env python3

class Automovil:
    
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
    
    @classmethod
    def deportivos(cls, marca):
        return cls(marca, "Deportivo") # cls es una referencia a la clase --> Automovil : cls(marca, "Deportivo")
    
    @classmethod
    def sedan(cls, marca):
        return cls(marca, "Sedan") # cls es una referencia a la clase --> Automovil : cls(marca, "Sedan")
    
    def __str__(self):
        return f"Marca: {self.marca} - Modelo: {self.modelo}"
        
deportivo = print(Automovil.deportivos("Ferrari"))
deportivo = print(Automovil.deportivos("Lamborghini"))
deportivo = print(Automovil.sedan("Toyota"))