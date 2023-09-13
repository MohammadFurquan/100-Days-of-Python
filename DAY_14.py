print("Day 14: 13/09/2023")

# CONDITIONAL OPERATORS
# >, <, >=, ==, !=

a = int(input("Enter any number: "))
print(a>18)
print(a<=18)
print(a==18)
print(a!=18)



# CONDITIONAL STATEMENT
# if the expression evaluates True: Execute the block of code inside if statement. After execution return to the code out of the if...else block
# if the expression evaluates False: Execute the block of code inside else statement. After execution return to the code out of the if...else block

a = int(input("Enter your age : "))
print("Your age is : ",a)

if(a>18):
    print("You can drive")
else:
    print("You cannot drive")


# if-else
applePrice = 210
budget = 200
if(applePrice <= budget):
    print("Alexa, add 1 kg Apples to the cart")
else:
    print("Alexa, do not add Apples to the cart")



# if-elif-else
num = int(input("Enter the value: "))
if(num<0):
    print("Number is negative")
elif(num == 0):
    print("Number is Zero")
else:
    print("Number is positive")



# if-elif-else
num = int(input("Enter the value: "))
if(num<0):
    print("Number is negative")
elif(num == 0):
    print("Number is Zero")
elif(num==999):
    print("Number is Special")
else:
    print("Number is positive")

print("I am Happy Now")



# nested-if-else
num = 18
if(num < 0):
    print("Number is negative")
elif(num > 0):
    if(num <= 10):
        print("Number is between 1-10")
    elif(num <= 20):
        print("Number is between 11-20")
    else:
        print("Number is greater than 20")
else:
    print("Number is Zero")
