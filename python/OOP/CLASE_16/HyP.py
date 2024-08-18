#!/usr/bin/env python3

class Dispositivo:
    
    def __init__(self, modelo):
        self.modelo = modelo
        
    def escanear_vulnerabilidades(self):
        raise NotImplementedError("La subclase debe implementar este método")
    
class Computadora(Dispositivo):
    
    def escanear_vulnerabilidades(self):
        return f"\n[+] Escaneando vulnerabilidades en la computadora {self.modelo}"

class Router(Dispositivo):
    
    def escanear_vulnerabilidades(self):
        return f"\n[+] Escaneando vulnerabilidades en el router {self.modelo}: \n\t[!] Vulnerabilidad en el puerto 80"

class Impresora(Dispositivo):
    
    def escanear_vulnerabilidades(self):
        return f"\n[+] Escaneando vulnerabilidades en la impresora {self.modelo}: \n\t[!] Vulnerabilidad en el puerto 515"
    
def escanear_dispositivo(dispositivo):
    print(dispositivo.escanear_vulnerabilidades())

computadora = Computadora("HP")
router = Router("Linksys")
impresora = Impresora("Epson")

escanear_dispositivo(computadora)
escanear_dispositivo(router)
escanear_dispositivo(impresora)

'''
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
'''

class Persona:
    
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
    def saludo(self):
        return f"\n[+] Hola, mi nombre es {self.nombre} y tengo {self.edad} años"
    
class Empleado(Persona):
    
    def __init__(self, nombre, edad, salario):
        super().__init__(nombre, edad)
        self.salario = salario
        
    def saludo(self):
        return f"\n {super().saludo()} y mi salario es de ${self.salario}"
    
persona = Persona("Juan", 25)
empleado = Empleado("Pedro", 30, 5000)

print(persona.saludo())
print(empleado.saludo())
