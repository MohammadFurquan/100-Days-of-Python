print("Day 21: 19/09/2023")

# Functions Argument
def average(a,b):
    print("The average is  ",(a+b)/2)

average(4,6)



def average(a=9,b=5):
    print("The average is  ",(a+b)/2)

average(4,6)



def average(a=9,b=5):
    print("The average is  ",(a+b)/2)

average()



def average(a=10,b=5):
    print("The average is  ",(a+b)/2)

average(6)



def average(a=10,b=5):
    print("The average is  ",(a+b)/2)

average(b=6)


# Returning a value from function
def average(a=10,b=5):
    return a+b

c = average(b=6)
print("The sum is :",c)




def average(*args):
    sum = 0
    print("Type of *args : ",type(args))    # TUPLE
    for i in args:
        sum+=i
    print("The sum is :",sum)

average(6,5,1,2,3,4,3,3,5,6,6,6,6,9)





def name(**name):
    print("Hello,", name["fname"],name["mname"],name["lname"])
    for i,j in name.items():
        print(i,j)

name(mname = "john", lname = "Barnes", fname = "James")

