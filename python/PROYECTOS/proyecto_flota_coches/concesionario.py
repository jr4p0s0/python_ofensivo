#!/usr/bin/env python3

class Vehiculo:
    
    def __init__(self, matricula: str, marca: str, modelo: str, precio: float) -> None:
        self.matricula = matricula
        self.marca = marca
        self.modelo = modelo
        self.precio = precio
        self.disponible = True
    
    def __str__(self) -> str:
        return f"\t [+] {self.marca} {self.modelo} ({self.matricula}) - {'Disponible' if self.disponible else 'No disponible'}"
        
class Concesionario:
    
    def __init__(self, nombre: str) -> None:
        self.nombre = nombre
        self.vehiculos = []
    
    def agregarVehiculo(self, vehiculo: Vehiculo) -> None:
        self.vehiculos.append(vehiculo)
        
    def mostrarVehiculos(self) -> None:
        for vehiculo in self.vehiculos:
            print(vehiculo)
    
    def alquilarVehiculo(self, matricula: str) -> None:
        for vehiculo in self.vehiculos:
            if vehiculo.matricula == matricula:
                if not vehiculo.disponible:
                    print(f"\n [!] El vehículo con la matrícula {matricula} no está disponible")
                    return
                vehiculo.disponible = False
                print(f"\n [!] Se ha alquilado el siguiente vehículo: {vehiculo}\n")
                return
        print(f"\n [!] No se encontró el vehículo con la matrícula {matricula}")
        
    def devolverVehiculo(self, matricula: str) -> None:
        for vehiculo in self.vehiculos:
            if vehiculo.matricula == matricula:
                if vehiculo.disponible:
                    print(f"\n [!] No se puede devolver un vehiculo que está disponible: {matricula} ya está disponible")
                    return
                vehiculo.disponible = True
                print(f"\n [!] Se ha devuelto el siguiente vehículo: {vehiculo}\n")
                return
        print(f"\n [!] No se encontró el vehículo con la matrícula {matricula}")
            
    def __str__(self) -> str: # vamos a mostrar la información del concesionario con los vehículos que tiene
        return "\n".join([f" [*] {self.nombre}"] + [str(vehiculo) for vehiculo in self.vehiculos])
        
    


if __name__ == "__main__":
    
    concesionario = Concesionario("Coches S.A.")
    
    concesionario.agregarVehiculo(Vehiculo("1234ABC", "Ford", "Focus", 15000))
    concesionario.agregarVehiculo(Vehiculo("5678DEF", "Renault", "Clio", 12000))
    concesionario.agregarVehiculo(Vehiculo("91011GHI", "Seat", "Ibiza", 13000))
    
    print(concesionario)
    
    concesionario.alquilarVehiculo("1234ABC")
    
    print(concesionario)
    
    concesionario.alquilarVehiculo("1234ABC")
    
    concesionario.devolverVehiculo("1234ABC")
    
    print(concesionario)
    
    concesionario.devolverVehiculo("1234ABC")