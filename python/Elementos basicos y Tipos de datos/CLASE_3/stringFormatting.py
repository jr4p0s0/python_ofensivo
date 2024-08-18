#!/usr/bin/env python3

# String Formatting

name = "j4im3"
rol = "student"

edad = 22

print("Hello, my name is %s, and I'm a %s. I'm %d" % (name, rol, edad)) # Hello, j4im3! 

# %s - String (or any object with a string representation, like numbers)
# %d - Integers
# %f - Floating point numbers
# %.<number of digits>f - Floating point numbers with a fixed amount of digits to the right of the dot.
# %x/%X - Integers in hex representation (lowercase/uppercase)
# %o - Integers in octal representation
# %r - String (converts any python object using repr())

#.format() method

print("Hello, my name is {}, and I'm a {}. I'm {}".format(name, rol, edad))

# f-strings

print(f"Hello, my name is {name}, and I'm a {rol}. I'm {edad}")

# f-strings are available in Python 3.6 and later versions.
# f-strings provide a concise and convenient way to embed python expressions inside string literals, using curly braces {}.
# f-strings are faster than both %-formatting and str.format().
# f-strings are more readable than both %-formatting and str.format().
# f-strings are more powerful than both %-formatting and str.format().
# f-strings can be used for any type of python expressions.

# f-strings are evaluated at runtime, so you can put any and as many valid python expressions as you want inside the curly braces.
# f-strings can be used to call functions, methods, and objects.
# f-strings can be used to access elements of lists, tuples, dictionaries, and sets.