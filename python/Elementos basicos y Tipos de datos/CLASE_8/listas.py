#!/usr/bin/env python3

# Lists

cve_list = ["CVE-2021-1234", "CVE-2021-5678", "CVE-2021-9101"]

# Accessing elements

print(cve_list[0]) # CVE-2021-1234
print(cve_list[1]) # CVE-2021-5678
print(cve_list[2]) # CVE-2021-9101

# Negative indexing

print(cve_list[-1]) # CVE-2021-9101
print(cve_list[-2]) # CVE-2021-5678
print(cve_list[-3]) # CVE-2021-1234

# Slicing

print(cve_list[0:2]) # ['CVE-2021-1234', 'CVE-2021-5678']

# Changing elements

cve_list[2] = "CVE-2021-1122"

print(cve_list) # ['CVE-2021-1234', 'CVE-2021-5678', 'CVE-2021-1122']

# Looping through a list

for cve in cve_list:
    print(cve)
    
# Checking if an element exists

if "CVE-2021-1234" in cve_list:
    print("CVE-2021-1234 is in the list!")
    
# List length

print(len(cve_list)) # 3

# Adding elements

cve_list.append("CVE-2021-3344")

print(cve_list) # ['CVE-2021-1234', 'CVE-2021-5678', 'CVE-2021-1122', 'CVE-2021-3344']

# Removing elements

cve_list.remove("CVE-2021-1234")

print(cve_list) # ['CVE-2021-5678', 'CVE-2021-1122', 'CVE-2021-3344']

# Removing elements by index

cve_list.pop(1)

print(cve_list) # ['CVE-2021-5678', 'CVE-2021-3344']

# Clearing a list

cve_list.clear()

print(cve_list) # []

# Copying a list

cve_list = ["CVE-2021-1234", "CVE-2021-5678", "CVE-2021-9101"]

cve_list_copy = cve_list.copy()

print(cve_list_copy) # ['CVE-2021-1234', 'CVE-2021-5678', 'CVE-2021-9101']

# Joining lists

cve_list_1 = ["CVE-2021-1234", "CVE-2021-5678", "CVE-2021-9101"]

cve_list_2 = ["CVE-2021-1122", "CVE-2021-3344"]

cve_list_3 = cve_list_1 + cve_list_2

print(cve_list_3) # ['CVE-2021-1234', 'CVE-2021-5678', 'CVE-2021-9101', 'CVE-2021-1122', 'CVE-2021-3344']

# Extending a list

cve_list_1 = ["CVE-2021-1234", "CVE-2021-5678", "CVE-2021-9101"]

cve_list_2 = ["CVE-2021-1122", "CVE-2021-3344"]

cve_list_1.extend(cve_list_2)

print(cve_list_1) # ['CVE-2021-1234', 'CVE-2021-5678', 'CVE-2021-9101', 'CVE-2021-1122', 'CVE-2021-3344']

# List constructor

cve_list = list(("CVE-2021-1234", "CVE-2021-5678", "CVE-2021-9101"))

print(cve_list) # ['CVE-2021-1234', 'CVE-2021-5678', 'CVE-2021-9101']

# List methods

# append() - Adds an element at the end of the list
# clear() - Removes all the elements from the list
# copy() - Returns a copy of the list
# count() - Returns the number of elements with the specified value
# extend() - Add the elements of a list (or any iterable), to the end of the current list
# index() - Returns the index of the first element with the specified value
# insert() - Adds an element at the specified position
# pop() - Removes the element at the specified position
# remove() - Removes the first item with the specified value
# reverse() - Reverses the order of the list
# sort() - Sorts the list

# List comprehension

# List comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list.

# Syntax: [expression for item in iterable if condition == True]

# Example:

numbers = [1, 2, 3, 4, 5]

squared_numbers = [x * x for x in numbers]

print(squared_numbers) # [1, 4, 9, 16, 25]

# Example:

numbers = [1, 2, 3, 4, 5]

even_numbers = [x for x in numbers if x % 2 == 0]

print(even_numbers) # [2, 4]

# Example:

numbers = [1, 2, 3, 4, 5]

odd_numbers = [x for x in numbers if x % 2 != 0]

print(odd_numbers) # [1, 3, 5]

# Example:

numbers = [1, 2, 3, 4, 5]

squared_even_numbers = [x * x for x in numbers if x % 2 == 0]

print(squared_even_numbers) # [4, 16]

lista1 =  [1, 2, 3, 4, 5]
lista2 = [6, 7, 8, 9, 10]

lista3 = list(lista1)

print(lista3) # [1, 2, 3, 4, 5]
