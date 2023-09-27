print("Day 29: 27/09/2023")

# DOCSTRINGS: Python docstrings are the string literals that appear right after the defination of a function, method, class or module

def square(n):
    '''Takes in a number n, return the
    square of n'''
    print(n**2)

square(5)
print(square.__doc__)



# By changing the COMMENT the output of the program will NOT CHANGED
# but By changing the DOCSTRING the output of the program will be CHANGED


# Comments are descriptions that help programmers better understand the intent and functionality of the program.
# They are completely ignored by the Python interpreter

# Docstring are strings used right after the defination of a function, method, class, or module(like in Example1)
# They are used to document out code.
# We can access the docstring using the doc attribute

import this
# Print "The Zen of Python"

