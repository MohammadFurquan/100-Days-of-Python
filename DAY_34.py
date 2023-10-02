print("Day 33: 1/10/2023")

# Dictionary Methods

ep1 = {122 : 45, 123 : 89, 567 : 69, 670 : 69}
ep2 = {222 : 67, 566 : 90}
ep1.update(ep2)
print(ep1)


ep2.clear()
print(ep2)


ep3 = {}
print(type(ep3))

ep1.pop(122)
print(ep1)

ep1.popitem()
print(ep1)

# Deleting Dictionary
# del ep1

# Deleting item
# del ep1[122]



