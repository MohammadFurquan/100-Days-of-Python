print("Day 38: 6/10/2023")

# Custom Error : using raise keyword

a = int(input("Enter any value betwee 5 and 9 : "))

if(a<5 or a>9):
    raise ValueError("Value should be between 5 and 9")


# it should not give error on if string given by user is 'quit'
# 2
a = input("Enter any value betwee 5 and 9 : ")
if(int(a)<5 or int(a)>9)  or (a.lower()=="quit"):
    raise ValueError("Value should be between 5 and 9 or 'quit' ")


