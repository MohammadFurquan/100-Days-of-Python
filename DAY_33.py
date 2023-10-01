print("Day 33: 1/10/2023")

# Dictionary
# Dictionary are the ordered collection of items and items are key-value pair and they are separated by commas and enclosed in { }
# Before version of 3.7 of Python Dictionary was Unordered


info = {
    344: "Harry",
    56: "Shubham",
    678: "Zakir",
    567: "Neha"
    
}


print(info)
print(info[56])
print(info.get(678))
print(info.get(699999999999978)) #Get wont give you error
print(info.keys())
print(info.values())
print(info.items())
print(info.popitem())
print(info.setdefault(444,"NOthing is here HeHe"))

for key,value in info.items():
    print(f"key --> {key} and values is {value}")


