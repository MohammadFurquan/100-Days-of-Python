print("Day 11: 10/09/2023")

# STRINGS : In python, anything that you enclose between single or double quotation makrs is considered a string.
# A string is essentially a sequence or array of textual data. Strings are used when working with unicode
# It does not matter whether you enclose your strings in single or double quotes, the output remains the same.

name = "Furquan"
print("Hello, " + name)


# apple = "He said, "I want to eat an apple"    #it will give error
apple = 'He said, "I want to eat an apple'  
print(apple)
apple = "He said, \"I want to eat an apple"
print(apple)


# Multi-line String
apple = ''' He said,
hey i am good
what about you'''
print(apple)


# Accessing characters of a string
name = "Furquan Faizi"
print(name[0])
print(name[1])
print(name[2])


# Looping through the string
name = "Furquan"
for i in name:
    print(i)


