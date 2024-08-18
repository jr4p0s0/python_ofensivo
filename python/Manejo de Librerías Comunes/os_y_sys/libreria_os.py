#!/usr/bin/env python3

import os

dir_path = os.getcwd()

print(f"\n [+] Directorio actual: {dir_path}")

files = os.listdir(dir_path)

print(f"\n [+] Archivos en el directorio actual: {files}")

if not os.path.exists("nuevo_directorio"): os.mkdir("nuevo_directorio")

print("\n [+] Nuevo directorio creado")

files = os.listdir(dir_path)

print(f"\n [+] Archivos en el directorio actual: {files}")

os.rmdir("nuevo_directorio")

get_env = os.getenv("PATH")

print(f"\n [+] Variable de entorno PATH: {get_env}")

get_env = os.getenv("KITTY_INSTALLATION_DIR")

print(f"\n [+] Variable de entorno KITTY_INSTALLATION_DIR: {get_env}")