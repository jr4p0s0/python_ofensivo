#!/usr/bin/env python3

# Treating Exceptions (Errors)

# Exceptions are errors that occur during the execution of a program.
# Exceptions are not unconditionally fatal.

# Syntax:

# try:
#     # code that may raise an exception
# except ExceptionName:
#     # code that handles the exception
# else:
#     # code that runs if no exception occurs
# finally:
#     # code that always runs

# Example:

try:
    print(5 / 1)
except ZeroDivisionError:
    print("You can't divide by zero!")
else:
    print("Division was successful!")
finally:
    print("This will always run!")
    
# launch exceptions

# raise Exception("This is an exception!")

x = -1

#if x < 0:
    #raise Exception("Sorry, no numbers below zero!")

# Custom Exceptions

class ValueTooSmallError(Exception):
    pass

class ValueTooLargeError(Exception):
    pass

number = 1

try:
    if number < 5:
        raise ValueTooSmallError("Value is too small!")
    elif number > 15:
        raise ValueTooLargeError("Value is too large!")
except ValueTooSmallError as e:
    print(e)
except ValueTooLargeError as e:
    print(e)
else:
    print("Value is just right!")
finally:
    print("This will always run!")
    
    