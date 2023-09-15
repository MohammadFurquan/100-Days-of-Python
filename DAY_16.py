print("Day 16: 15/09/2023")

# MATCH CASE STATEMENT 
# Match case statement is in Python 3.10

x = 88

match x:
    case 0:
        print("x is zero")
    case 4:
        print("case is 4")
    case _ if(x!=90):
        print(x," is not 90")
    case _ if x!=80:
        print(x," is not 80")
    case _: #default
        print(x)

# There is no need to use break statement in python in match case