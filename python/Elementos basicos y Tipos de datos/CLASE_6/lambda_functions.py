#!/usr/bin/env python3

# Lambda Functions (Anonymous Functions)

my_function = lambda: "Hello, World!"

print(my_function()) # Hello, World!

# Lambda functions are small anonymous functions that can have any number of arguments, but can only have one expression.

# Syntax: lambda arguments: expression

square = lambda x: x * x

print(square(5)) # 25

# Lambda functions can take any number of arguments:

add = lambda x, y: x + y

print(add(5, 3)) # 8

# real world example

numbers = [1, 2, 3, 4, 5]

squared_numbers = list(map(lambda x: x * x, numbers))

print(squared_numbers) # [1, 4, 9, 16, 25]

# real world example
# sorting a list of tuples by the second element

students = [("j4im3", 22), ("j4im3", 21), ("j4im3", 23), ("j4im3", 20)]
print(students)

students.sort(key=lambda x: x[1]) # sort by age
# students.sort(key=lambda x: x[0]) # sort by name
print(students)

# Using lambda functions with filter()

numbers = [1, 2, 3, 4, 5]

even_numbers = list(filter(lambda x: x % 2 == 0, numbers))

print(even_numbers) # [2, 4]

# Using lambda functions with reduce()

from functools import reduce

numbers = [1, 2, 3, 4, 5]

sum_of_numbers = reduce(lambda x, y: x + y, numbers)

print(sum_of_numbers) # 15
print(type(sum_of_numbers)) # <class 'int'>

mult_of_numbers = reduce(lambda x, y: x * y, numbers)
print(mult_of_numbers) # 120