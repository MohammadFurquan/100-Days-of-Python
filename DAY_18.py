print("Day 18: 17/09/2023")

# WHILE : AS THE NAME SUGGESTS WHILE LOOPS EXECUTE STATEMENTS WHILE THE CONDITON IS TRUE.
# AS SOON AS THE CONDITON BECOMES FALSE,THE INTERPRETER COMES OUT OF THE WHILE LOOP.


i = 0
while(i<3):
    print(i)
    i = i + 1

i = 0
while(i<=3):
    print(i)
    i+=1

# It will take input ultil i give value as 1
ls = []
i = 0
while i!=1:
    i = int(input("Enter element of list: "))
    ls.append(i)
print(ls)


# Decrementing Loop
count = 5
while count>0:
    print(count)
    count = count - 1


# While loop with else
count = 5
while count>0:
    print(count)
    count = count - 1
else:
    print("I am inside else")

