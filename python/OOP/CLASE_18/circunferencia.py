#!/usr/bin/env python3

class Circunferencia:
    
    # def __init__(self, radio):
    #     self._radio = radio
        
    def __str__(self):
        return f"Radio: {self._radio}"
    
    @property # Getter
    def radio(self):
        return self._radio
    
    @radio.setter
    def radio(self, radio):
        if radio <= 0:
            raise ValueError("[!] El radio no puede ser negativo o cero")
        self._radio = radio
        
    @property
    def diametro(self):
        return self._radio * 2
    
    @property
    def area(self):
        return 3.14159286 * (self._radio ** 2)
    
    @property
    def perimetro(self):
        return 2 * 3.14159286 * self.radio
    
class Circ(Circunferencia):
    def __init__(self, radio):
        super().__init__()
    
    
c = Circ(1)