#!/usr/bin/python3

class Libro:
    
    def __init__(self, id: int, titulo: str, autor: str, editorial: str, paginas: int, ISBN: int) -> None:
        self.id = id
        self.titulo = titulo
        self.autor = autor
        self.editorial = editorial
        self.paginas = paginas
        self.ISBN = ISBN # International Standard Book Number (ISBN) --> id único de un libro
        self.prestado = False 

    def __str__(self) -> str:
        return f"Libro: '{self.titulo}' de '{self.autor}' ({self.editorial})"
    
    def __repr__(self) -> str:
        return self.__str__()


class Biblioteca:
        
    def __init__(self) -> None:
        self.libros = {}
    
    def agregar_libro(self, libro: Libro) -> None:
        if libro.id not in self.libros:
            self.libros[libro.id] = libro
        else: 
            print(f" [!] El libro con ID {libro.id} ya existe en la biblioteca")
    
    def prestar_libro(self, id: int) -> Libro:
        if id in self.libros and not self.libros[id].prestado:
            self.libros[id].prestado = True
            return self.libros[id]
    
    def devolver_libro(self, titulo: str) -> Libro:
        libro = self.buscar_libro(titulo)
        if libro:
            if libro.prestado:
                libro.prestado = False
                return libro
            else:
                return print(f" [!] El libro '{titulo}' no está prestado")
        else:
            return print(f" [!] El libro '{titulo}' no se encuentra en la biblioteca")
    
    @property
    def mostrar_libros(self):
        return [libro for libro in self.libros.values() if not libro.prestado]
    
    @property
    def mostrar_libros_prestados(self):
        return [libro for libro in self.libros.values() if libro.prestado]

class BibliotecaInfantil(Biblioteca):
    
    def __init__(self) -> None:
        super().__init__()
        self.libros_infantiles = {} # -> {1: True, 2: False, 3: True} -> {id: para niños o no}
        
    def agregar_libro(self, libro: Libro, es_para_ninos: bool) -> None:
        super().agregar_libro(libro) 
        self.libros_infantiles[libro.id] = es_para_ninos 
    
    def prestar_libro(self, id: int, es_para_nino: bool) -> Libro:
        if (id in self.libros) and (not self.libros[id].prestado) and (self.libros_infantiles[id] == es_para_nino):
            self.libros[id].prestado = True
        else:
            print(f"\n [!] No se puede prestar el libro con id {id}")

if __name__ == "__main__":
    
    libro1 = Libro(1, "El Quijote", "Cervantes", "Anaya", 1000, 123456789)
    libro2 = Libro(2, "El Señor de los Anillos", "Tolkien", "Santillana", 2000, 987654321)
    
    print(libro1)
    print(libro2)
    
    biblioteca = BibliotecaInfantil()
    
    biblioteca.agregar_libro(libro1, es_para_ninos=False)
    biblioteca.agregar_libro(libro2, es_para_ninos=True)
    
    print(f"\n [+] Libros en la biblioteca: {biblioteca.mostrar_libros}")
    
    biblioteca.prestar_libro(1, es_para_nino=False)
    
    print(f"\n [+] Libros en la biblioteca: {biblioteca.mostrar_libros}")
    print(f"\n [+] Libros prestados: {biblioteca.mostrar_libros_prestados}")
    
    biblioteca.prestar_libro(1, es_para_nino=False)
    biblioteca.prestar_libro(2, es_para_nino=True)
    print(f"\n [+] Libros prestados: {biblioteca.mostrar_libros_prestados}")
    
    print(f"\n [+] Libros para niños: {biblioteca.libros_infantiles}")
    
