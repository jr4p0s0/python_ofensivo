#!/usr/bin/env python3

class Nota:
        
    def __init__(self, contenido: str) -> None:
        self.contenido = contenido
        
    def __str__(self) -> str:
        return self.contenido