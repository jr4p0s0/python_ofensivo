#!/usr/bin/env python3

tope = 500 # Tope de ventas

juegos = ["Super Mario Bros", "Zelda: Breath of the Wild", "Cyberpunk 2077", "Final Fantasy VII"]

# Géneros --> diccionario

generos = {
    "Super Mario Bros": "Aventura",
    "Zelda: Breath of the Wild": "Aventura",
    "Cyberpunk 2077": "ROL",
    "Final Fantasy VII": "ROL",
}

# Ventas y stock --> tupla

ventas_y_stock = {
    "Super Mario Bros": (400, 200),
    "Zelda: Breath of the Wild": (300, 15),
    "Cyberpunk 2077": (39, 50),
    "Final Fantasy VII": (892, 3),
} 

# Clientes --> set

clientes = {
    "Super Mario Bros": {"Juan", "Pedro", "María", "Ana", "Luis"},
    "Zelda: Breath of the Wild": {"Juan", "Pedro", "María"},
    "Cyberpunk 2077": {"Ana", "Luis"},
    "Final Fantasy VII": {"Juan", "Pedro", "María", "Ana", "Luis", "Carlos", "David"},
}


def sumario(juego):
    # Sumario
    print(f"\n[INFO] RESUMEN DEL JUEGO {juego}\n")
    print(f"\t[+] Género: {generos[juego]}")
    print(f"\t[+] Ventas: {ventas_y_stock[juego][0]} unidades")
    print(f"\t[+] Stock: {ventas_y_stock[juego][1]} unidades")
    print(f"\t[+] Clientes que han adquirido el juego: {', '.join(clientes[juego])}\n")
    
for juego in juegos:
    if ventas_y_stock[juego][0] > tope: # Si las ventas superan las 500 unidades
        sumario(juego)

ventas_totales = lambda x: sum([x[juego][0] for juego in x]) # Ventas totales 
ventas_totales_sin_parametros = lambda: sum(ventas for juego, (ventas, _) in ventas_y_stock.items() if ventas_y_stock[juego][0] > tope) # Ventas totales sin parámetros

print(f"\n[INFO] VENTAS TOTALES: {ventas_totales(ventas_y_stock)} unidades\n")
print(f"[INFO] VENTAS TOTALES (sin parámetros): {ventas_totales_sin_parametros()} unidades\n")

