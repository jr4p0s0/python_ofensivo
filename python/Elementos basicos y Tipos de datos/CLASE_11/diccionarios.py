#!/usr/bin/env python3

# Dictionaries

# Dictionaries are unordered, changeable, and indexed collections of elements.
# Dictionaries are written with curly brackets.
# Dictionaries are mutable, meaning that you can change, add, or remove items after the dictionary has been created.
# Dictionaries are used to store data values in key:value pairs.

# Creating a dictionary

cve_dict = { "cve-2021-1234": "Vulnerability in X", "cve-2021-5678": "Vulnerability in Y", "cve-2021-9101": "Vulnerability in Z" }

# Accessing elements

print(cve_dict["cve-2021-1234"]) # Vulnerability in X

diccionario_j4im3 = { "nombre": "Jaime", "edad": 25, "ciudad": "CDMX", "hobbies": ["leer", "correr", "nadar"] }

print(diccionario_j4im3["nombre"]) # Jaime
print(diccionario_j4im3["edad"]) # 25
print(diccionario_j4im3["ciudad"]) # CDMX

# Changing elements

diccionario_j4im3["edad"] = 26

print(diccionario_j4im3["edad"]) # 26

# Adding elements

diccionario_j4im3["profesion"] = "Ingeniero en Sistemas"

print(diccionario_j4im3) # {'nombre': 'Jaime', 'edad': 26, 'ciudad': 'CDMX', 'hobbies': ['leer', 'correr', 'nadar'], 'profesion': 'Ingeniero en Sistemas'}

# Removing elements

diccionario_j4im3.pop("ciudad")

print(diccionario_j4im3) # {'nombre': 'Jaime', 'edad': 26, 'hobbies': ['leer', 'correr', 'nadar'], 'profesion': 'Ingeniero en Sistemas'}

# Looping through a dictionary

for key in diccionario_j4im3:
    print(key) # nombre, edad, hobbies, profesion

for key in diccionario_j4im3:
    print(diccionario_j4im3[key]) # Jaime, 26, ['leer', 'correr', 'nadar'], Ingeniero en Sistemas

for key, value in diccionario_j4im3.items():
    print(key, value) # nombre Jaime, edad 26, hobbies ['leer', 'correr', 'nadar'], profesion Ingeniero en Sistemas
    
# Copying a dictionary

diccionario_j4im3_copia = diccionario_j4im3.copy()

print(diccionario_j4im3_copia) # {'nombre': 'Jaime', 'edad': 26, 'hobbies': ['leer', 'correr', 'nadar'], 'profesion': 'Ingeniero en Sistemas'}

# Nested dictionaries

diccionario_j4im3["contacto"] = { "email": "jaime@mail.com", "telefono": "555-555-5555" }

print(diccionario_j4im3) # {'nombre': 'Jaime', 'edad': 26, 'hobbies': ['leer', 'correr', 'nadar'], 'profesion': 'Ingeniero en Sistemas', 'contacto': {'email': '

print(diccionario_j4im3["contacto"]["email"]) # {'email': 'jaime@mail.com' }

# Dictionary methods

# clear() - Removes all the elements from the dictionary
# copy() - Returns a copy of the dictionary
# fromkeys() - Returns a dictionary with the specified keys and values
# get() - Returns the value of the specified key
# items() - Returns a list containing a tuple for each key value pair
# keys() - Returns a list containing the dictionary's keys
# pop() - Removes the element with the specified key
# popitem() - Removes the last inserted key-value pair
# setdefault() - Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
# update() - Updates the dictionary with the specified key-value pairs
# values() - Returns a list of all the values in the dictionary
# concat() - Concatenates dictionaries

# Example

print(diccionario_j4im3.keys()) # dict_keys(['nombre', 'edad', 'hobbies', 'profesion', 'contacto'])

print(diccionario_j4im3.values()) # dict_values(['Jaime', 26, ['leer', 'correr', 'nadar'], 'Ingeniero en Sistemas', {'email': '

print(diccionario_j4im3.items()) # dict_items([('nombre', 'Jaime'), ('edad', 26), ('hobbies', ['leer', 'correr', 'nadar']), ('profesion', 'Ingeniero en Sistemas'), ('contacto', {'email': '

print(diccionario_j4im3.get("nombre")) # Jaime

print(diccionario_j4im3.popitem()) # ('contacto', {'email': ' [email protected]', 'telefono': '555-555-5555'})

print(diccionario_j4im3) # {'nombre': 'Jaime', 'edad': 26, 'hobbies': ['leer', 'correr', 'nadar'], 'profesion': 'Ingeniero en Sistemas'}

if "nombre" in diccionario_j4im3:
    print("El nombre es Jaime")

