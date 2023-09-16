print("Day 17: 16/09/2023")

# LOOPS : WHEN WE WANT TO EXECUTE A GROUP OF STATEMENTS MULTIPLE TIMES WE USE LOOPS
# For loops can iterate over a sequence of iterable objects in Python

# Example : i want to print number from 1 to 100
print(1)
print(2)
print(3)
print(4)

name = "Furquan"
for i in name:
    print(i)

for i in name:
    if(i=="b"):
        print("This is something special!!!!")


colors = ["Red", "Green","Blue","Yellow"]
for color in colors:
    print(color)


# Range() Function
for k in range(5):
    print(k)

for k in range(5):
    print(k+1)

for i in range(11,21):
    print(i)

for i in range(11,21,2):
    print(i)


