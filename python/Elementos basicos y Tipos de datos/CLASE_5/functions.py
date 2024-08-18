#!/usr/bin/env python3

# defining a function

def greet(name, rol, edad):
    return f"Hello, my name is {name}, and I'm a {rol}. I'm {edad}"

# calling the function

print(greet("j4im3", "student", 22)) # Hello, my name is j4im3, and I'm a student. I'm 22

# defining a function with default values

def greet(name="j4im3", rol="student", edad=22):
    
    return f"Hello, my name is {name}, and I'm a {rol}. I'm {edad}"

# calling the function

print(greet()) # Hello, my name is j4im3, and I'm a student. I'm 22

# calling the function with positional arguments

print(greet("j4im3", "student", 22)) # Hello, my name is j4im3, and I'm a student. I'm 22

# calling the function with keyword arguments

print(greet(name="j4im3", rol="student", edad=22)) # Hello, my name is j4im3, and I'm a student. I'm 22

# calling the function with keyword arguments in a different order

print(greet(rol="student", name="j4im3", edad=22)) # Hello, my name is j4im3, and I'm a student. I'm 22

# calling the function with a mix of positional and keyword arguments

print(greet("j4im3", rol="student", edad=22)) # Hello, my name is j4im3, and I'm a student. I'm 22

# calling the function with a mix of positional and keyword arguments in a different order

print(greet("j4im3", edad=22, rol="student")) # Hello, my name is j4im3, and I'm a student. I'm 22

# global and local variables

# defining a global variable

name = "j4im3"

def greet(rol, edad):
        
        # defining a local variable
        
        name = "j4im3"
        
        return f"Hello, my name is {name}, and I'm a {rol}. I'm {edad}"
    
# calling the function

print(greet("student", 22)) # Hello, my name is j4im3, and I'm a student. I'm 22

# defining a global variable

def greet(rol, edad):
        
        # using the global variable
        
        global name
        
        return f"Hello, my name is {name}, and I'm a {rol}. I'm {edad}"

# calling the function

print(greet("student", 22)) # Hello, my name is j4im3, and I'm a student. I'm 22
    