#!/usr/bin/env python3

class Rectangulo:
    
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
    
    @property
    def area(self):
        return self.base * self.altura
    
    def __str__(self):
        return f"\n [*] Propiedades del rectángulo: \n\t [+] Base {self.base} \n\t [+] Altura {self.altura}."

rect1 = Rectangulo(10, 20)

print(rect1)
print(f"El área del rectángulo es de {rect1.area} unidades cuadradas.")


class Libro:
    
    best_seller_value = 100000
    IVA = 1.21
    
    def __init__(self, titulo, autor, paginas):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas
    
    @staticmethod # Método estático --> usando decorador @staticmethod 
    def es_best_seller(total_ventas):
        return total_ventas > Libro.best_seller_value
    
    @classmethod # Método de clase --> usando decorador @classmethod
    def precio_con_iva(cls, precio):
        return precio * cls.IVA
    
class LibroDigital(Libro):
    
    IVA = 1.10
    

libro1 = Libro("Python para todos", "Juan Perez", 200)
libro2 = LibroDigital("Python para todos", "Juan Perez", 200)

print(f"\n [*] Propiedades del libro: \n\t [+] Título: {libro1.titulo} \n\t [+] Autor: {libro1.autor} \n\t [+] Páginas: {libro1.paginas}.")
print(f"¿Es best seller? {Libro.es_best_seller(1000000)}")

print(f"\n [*] Propiedades del libro digital: \n\t [+] Título: {libro2.titulo} \n\t [+] Autor: {libro2.autor} \n\t [+] Páginas: {libro2.paginas}.")
print(f"¿Es best seller? {Libro.es_best_seller(1000000)}")

print(f"\n [*] Precio con IVA del libro: {round(Libro.precio_con_iva(100),2)}")
print(f" [*] Precio con IVA del libro digital: {round(LibroDigital.precio_con_iva(100))}")