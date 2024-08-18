#!/usr/bin/env python3

import os
from gestor_notas import GestorNotas

def main():
    
    gestor = GestorNotas()
    
    while True:
        print(f"\n--------------------\nMENÚ\n--------------------")
        print("1. Crear una nota")
        print("2. Mostrar todas las notas")
        print("3. Buscar una nota")
        print("4. Eliminar una nota")
        print("5. Salir")
        
        opcion = input("\n [?] Introduce una opción: ")
        
        if opcion == "1": # crear una nota
            contenido = input("\n [+] Introduce el contenido de la nota: ")
            gestor.agregar_nota(contenido)
        
        elif opcion == "2":
            notas = gestor.leer_notas()
            
            if notas:
                print("\n [+] Mostrando todas las notas almacenadas: \n")
                
                for i, nota in enumerate(notas):
                    print(f"\n Nota {i+1}: {nota}")
            else:    
                print("\n [!] No hay notas almacenadas")
                
        elif opcion == "3":
            contenido = input("\n [+] Introduce el contenido de la nota a buscar: ")
            notas = gestor.buscar_nota(contenido)
            print(f"\n [+] Notas encontradas: ")
            if notas:
                for i, nota in enumerate(notas):
                    print(f"\n Nota {i+1}: {nota}")        
            else:
                print(f"\n [!] No se encontraron notas con el contenido {contenido}")
        
        elif opcion == "4":
            print("\n [+] Elige la nota a eliminar: \n")
            notas = gestor.leer_notas()
            for i, nota in enumerate(notas):
                print(f"\n Nota {i}: {nota}")
            try:
                index = int(input("\n [?] Introduce el número de la nota a eliminar: "))
                gestor.eliminar_nota(index)
                print("\n [+] Nota eliminada correctamente")
            except ValueError:
                print("\n [!] Debes introducir un número")
            except IndexError:
                print("\n [!] No existe la nota seleccionada")
            
        elif opcion == "5":
            break
        
        elif opcion == '':
            os.system('cls' if os.name == 'nt' else 'clear')
            continue
        
        else:
            print("\n [!] Opción no válida")
        
        input("\n [+] Presiona <Enter> para continuar...")
        os.system('cls' if os.name == 'nt' else 'clear')
        



if __name__ == "__main__":
    main()