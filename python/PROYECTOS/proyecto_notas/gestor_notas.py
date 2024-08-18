#!/usr/bin/env python3

import pickle
from nota import Nota

class GestorNotas:
    
    def __init__(self, archivo_notas='notas.pkl') -> None:
        self.archivo_notas = archivo_notas
        
        try: 
            with open(self.archivo_notas, 'rb') as f:
                self.notas = pickle.load(f)
                print(f"\n [!] Se han cargado {len(self.notas)} notas")
        except FileNotFoundError:
            self.notas = []
    
    def guardar_notas(self) -> None:
        with open(self.archivo_notas, 'wb') as f:
            pickle.dump(self.notas, f)
            
    def agregar_nota(self, contenido: str) -> None:
        self.notas.append(Nota(contenido))
        self.guardar_notas()
    
    def leer_notas(self) -> None:
        return self.notas
    
    def buscar_nota(self, contenido: str) -> None:
        return [nota for nota in self.notas if contenido in nota.contenido]
    
    def eliminar_nota(self, index: int) -> None:
        del self.notas[index]
        self.guardar_notas()