#!/usr/bin/env python3

# Tuples

# Tuples are ordered and unchangeable collections of elements.
# Tuples are written with round brackets.
# Tuples are immutable, meaning that you cannot change, add, or remove items after the tuple has been created.

# Creating a tuple

cve_tuple = ("CVE-2021-1234", "CVE-2021-5678", "CVE-2021-9101")
# Actually, a tuple can have more than 2 elements, but this is just an example.

# Accessing elements

print(cve_tuple[0]) # CVE-2021-1234
print(cve_tuple[1]) # CVE-2021-5678
print(cve_tuple[2]) # CVE-2021-9101

# Negative indexing

print(cve_tuple[-1]) # CVE-2021-9101
print(cve_tuple[-2]) # CVE-2021-5678
print(cve_tuple[-3]) # CVE-2021-123

# Slicing

print(cve_tuple[0:2]) # ('CVE-2021-1234', 'CVE-2021-5678')

# Changing elements

# cve_tuple[2] = "CVE-2021-1122" # TypeError: 'tuple' object does not support item assignment

# Looping through a tuple

for cve in cve_tuple:
    print(cve)
    
# Checking if an element exists

if "CVE-2021-1234" in cve_tuple:
    print("CVE-2021-1234 is in the tuple!")


# Tuple length

print(len(cve_tuple)) # 3

# Adding elements

# cve_tuple.append("CVE-2021-3344") # AttributeError: 'tuple' object has no attribute 'append'

# Removing elements

# cve_tuple.remove("CVE-2021-1234") # AttributeError: 'tuple' object has no attribute 'remove'

# Removing elements by index

# cve_tuple.pop(1) # AttributeError: 'tuple' object has no attribute 'pop'

# Clearing a tuple

# cve_tuple.clear() # AttributeError: 'tuple' object has no attribute 'clear'

# Tuple methods

# count() - Returns the number of times a specified value occurs in a tuple.
# index() - Searches the tuple for a specified value and returns the position of where it was found.
# len() - Returns the number of elements in the tuple.

# Example

print(cve_tuple.count("CVE-2021-1234")) # 1
print(cve_tuple.index("CVE-2021-1234")) # 0

# Tuple unpacking

cve1, cve2, cve3 = cve_tuple

print(cve1) # CVE-2021-1234
print(cve2) # CVE-2021-5678
print(cve3) # CVE-2021-9101

# Tuple constructor

cve_tuple = tuple(("CVE-2021-1234", "CVE-2021-5678", "CVE-2021-9101"))

print(cve_tuple) # ('CVE-2021-1234', 'CVE-2021-5678', 'CVE-2021-9101')

# Tuple with one element

cve_tuple = ("CVE-2021-1234",)

print(type(cve_tuple)) # <class 'tuple'>

# Tuple without round brackets

cve_tuple = "CVE-2021-1234", "CVE-2021-5678", "CVE-2021-9101"

print(type(cve_tuple)) # <class 'tuple'>
