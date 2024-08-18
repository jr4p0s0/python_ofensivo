#!/usr/bin/env python3

import re

text = "Hola, mi número de teléfono es 123456789 y mi correo es johnDue@mail.com"

matches = re.findall(r"\d{9}", text) # busca un número de 9 dígitos
matches2 = re.findall(r"\w+@\w+\.\w+", text) # busca un correo
matches3 = re.findall("mi", text) # busca la palabra "mi"

print(matches)
print(matches2)
print(matches3)

text = "Hoy es 12/12/2021 y mañana será 13/12/2021"

matches = re.findall(r"\d{2}/\d{2}/\d{4}", text) # busca fechas en formato dd/mm/yyyy

print(matches)

text = "Los usuarios pueden contactar a los administradores a través de los correos: soporte@empresa.com y info@empresa.com"

# Vamos a almacenar los correos como una lista de tuplas (usuario, dominio)

matches = re.findall(r"(\w+)@(\w+\.\w+)", text)

print(matches)

print("\n [+] Usuarios encontrados para el dominio empresa.com: \n")
print([t[0] for t in matches if t[1] == "empresa.com"])

text = "campo1,campo2,campo3,campo4,campo5;campo6,campo7;campo8"

# Vamos a separar los campos por comas y punto y coma

matches = re.split(r"[;]", text)
for match in matches:
    print(re.split(r"[,]", match))

print(matches)


'''
+-----------------------------------------------+
'''

def validar_correo(correo):
    patron = "[a-zA-Z0-9_+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9]+"
    
    if re.match(patron, correo):
        return True
    else:
        return False
    
print(validar_correo("correoEjemplo@ejemplo.com"))

text = "Hoy es 12/12/2021 y mañana será 13/12/2021"

patron = r"(\d{2})/(\d{2})/(\d{4})"

for match in re.finditer(patron, text):
    print(f"La fecha es: {match.group(0)}, la cual comienza en la posición {match.start()} y termina en la posición {match.end()}")


