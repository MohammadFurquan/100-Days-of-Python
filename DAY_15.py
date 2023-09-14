print("Day 15: 14/09/2023")

# EXERCISE : IF-ELIF-ELSE

import time
timestamp = time.strftime('%H:%M:%S')
print(timestamp)

timestamp = time.strftime('%H')
print(timestamp)



import time
name = input("Enter Your Name: ").title()
# currentTime = time.strftime('%H:%M:%S')
# print(currentTime)
hour = int(ime.strftime('%H'))
if 4<=hour<12:
    print("Good Morning",name)
elif 12<=hour<17:
    print("Good Afternoon", name)
elif 17<=hour<21:
    print("Good Evening",name)
else:
    print("Good Night",name)


