#!/usr/bin/env python3

from time import sleep

class Animal:
    
    def __init__(self, nombre: str, especie: str) -> None:
        self.nombre = nombre
        self.especie = especie
        self.alimentado = False 
    
    def __str__(self) -> str:
        return f"\t [+] {self.nombre} ({self.especie}) - {'Alimentado' if self.alimentado else 'No alimentado'}"
    
    def alimentar(self) -> None:
        self.alimentado = True
        
    def vender(self) -> None:
        self.alimentado = False

class TiendaAnimales: # singleton -> solo una instancia de la clase 
    
    def __init__(self, nombre: str) -> None:
        self.nombre = nombre
        self.animales = []

    def agregarAnimal(self, animal: Animal) -> None:
        self.animales.append(animal)
        
    def mostrarAnimales(self) -> None:
        for animal in self.animales:
            print(animal)
    
    def alimentarAnimales(self) -> None:
        for animal in self.animales:
            animal.alimentar()
    
    def venderAnimal(self, nombre: str) -> None:
        for animal in self.animales:
            if animal.nombre == nombre:
                self.animales.remove(animal)
                animal.vender()
                print(f"\n [!] Venta realizada: {animal}")
                return
        print(f"\n [!] No se encontró el animal con el nombre {nombre}")


if __name__ == "__main__":
    
    tienda = TiendaAnimales("MascoShop")
    
    gato = Animal("Tito", "Gato")
    perro = Animal("Juan", "Perro")
    
    tienda.agregarAnimal(gato)
    tienda.agregarAnimal(perro)
    
    tienda.mostrarAnimales()
    tienda.alimentarAnimales()
    
    print(f"\n [!] Alimentando a los animales...\n")
    
    # esperar 2 segundos
    sleep(2)
    
    tienda.mostrarAnimales()
    
    tienda.venderAnimal("Tito")
    
    print(f"\n [!] Animales en la tienda: ") 
    tienda.mostrarAnimales()
    
    tienda.venderAnimal("Tito")
    
    