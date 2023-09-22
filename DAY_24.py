print("Day 24: 22/09/2023")

# TUPLE : Tuple are order collection of data items. They store  multiple items in a single variable. They are enclosed within round brackets.
# They are immutable

tup = (1,2,4,5)
print(type(tup))

t1 = (1,)
print(type(t1))

t2 = (1,2,3,3,"Faizi",True)
print(type(t2))
print(t2[0])
print(t2[-2])
print(len(t2))

if "Faizi" in t2:
    print("Yes Faizi is present in t2")

t3 = t2[1:4]
print(t3)








