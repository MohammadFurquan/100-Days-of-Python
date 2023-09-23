print("Day 25: 23/09/2023")


# Methods of Tuple

# Tuple is immutable but if we want to change in Tuple we can convert Tuple into List then we can do changes then again we can convert into Tuple
countries = ("Spain","Italy","India","England","Germany")
temp = list(countries)
temp.append("Russia")
temp.pop(3)
temp[2] = "Finland"
countries = tuple(temp)
print(countries)

# Tuple Concatenation
countries = ("India","Pakistan","England")
countries2 = ("China","Shrilanka","Bangladesh")
count = countries + countries2
print(count)

c = (countries,countries2)
print(c)


Tuple1 = (0,1,2,3,4,32,3,4,34,34,45,435,43,5,66)
print(Tuple1.count(3))
print(Tuple1.index(3))
print(Tuple1.index(3,4,8)) #it will find index of 3 between index no 4 to index no 8



