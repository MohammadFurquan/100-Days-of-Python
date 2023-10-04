print("Day 36: 4/10/2023")

# Exception Handling : Try Except

a = input("Enter the number : ")
print(f"Multiplication table of {a} is : ")

try : 
    for i in range(1,11):
        print(f"{int(a)} X {i} = {int(a)*i}")

except Exception as e:
    print(e)
    print("Sorry some error occured")
    print("Invalid Input")

print("Some imp lines of code")
print("End of Program")


# 2
try:
    num = int(input("Enter an integer : "))
except ValueError:
    print("Number entered is not an integer")

