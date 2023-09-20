print("Day 22: 20/09/2023")

# LIST : stores multiple items in a single variable in ordered way, items are separated by commas and enclosed within [] and they are mutable
l = [3,4,6]
print(type(l))
print(l)


# Accessing elements
marks = [3,5,6]
print(marks[0])
print(marks[1])
print(marks[2])


ls = [3,4,6,5.5,"Faizi",True]
print(ls[4])
print(ls[5])


# Negative indexing
ls = [3,4,6,5.5,"Faizi",True]
print(len(ls))
print(ls[-1])
print(ls[-2])
print(ls[len(ls)-2])


# If Else
ls = [3,4,6,5.5,"Faizi",True]
if "Faizi" in ls:
    print("Yes")
else:
    print("No")


# Slicing
ls = [3,4,6,5.5,"Faizi",True]
print(ls[1:-1])


lst = [ i for i in range(4)]
print(lst)


lst = [ i*i for i in range(4)]
print(lst)


