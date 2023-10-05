print("Day 37: 5/10/2023")

# Finally Clause
# Finally always execute
# Finally will execute even after returning the function 
def func1():
    try:
        l = [1,5,6,7]
        i = int(input("Enter the index : "))
        print(l[i])

    except:
        print("Some error occured")
        return 1

    finally:
        print("I am always executed")

    # print("Yes, I am also Executed!!!")


x = func1()
print(x)


