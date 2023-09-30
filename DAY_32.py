print("Day 32: 30/09/2023")

s1 = {1,2,5,6}
s2 = {3,6,7}
print(s1.union(s2))


s1 = {1,2,5,6}
s2 = {3,6,7}
print(s1.intersection(s2))


s1 = {1,2,5,6}
s2 = {3,6,7}
print(s1.update(s2))


alpha = {"Apple","BAll","Cat","Dog"}
alpha2 = {"BAll","Dog","Elephant","Fish"}
alpha3 = alpha.symmetric_difference(alpha2) # escape the common elements
print(alpha3)


alpha = {"Apple","BAll","Cat","Dog"}
alpha2 = {"BAll","Dog","Elephant","Fish"}
print(alpha.difference(alpha2))

