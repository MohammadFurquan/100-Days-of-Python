print("Day 23: 21/09/2023")

#List Methods

l = [1,2899,23,3,45,456,546,34,23,234,3,24,6,61,2,3,5,6,5,3,45,5]
print(l)

print(l.index(2899))

print(l.count(3))

l.append("Faizi")
print(l)

l.extend("Furquan")
print(l)

l.remove('F')
print(l)

l.insert(1,"Furquan Faizi")
print(l)

l.reverse()
print(l)

l.pop()
print(l)

l.pop(1)
print(l)

x = l.copy()
print(x)

x.clear()
print(x)


l = [1,2,3,5,2,2,1,18,9,56,3,43,2,31,2,124,57,8,342]
y = sorted(l)
print(y)
print(l)

l.sort(reverse=True)
print(l)

x = min(l)
print(x)

y = max(l)
print(y)

z = sum(l)
print(z)

