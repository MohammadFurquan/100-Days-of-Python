print("Day 30: 28/09/2023")

# RECURSION : Function Calling itself is called as Recursion

# Finding factorial using Recursion
def factorial(num):
    if num == 0:
        return 1
    
    return num * factorial(num - 1 )

result = factorial(5)
print("The Factorial of num is {}".format(result))
