print("Day 26: 24/09/2023")

# EXERCISE
import time
t = time.strftime('%H:%M:%S')
hour = int(time.strftime('%H'))
hour = int(input("Enter hour: "))
# print(hour)

if(hour>=0 and hour<12):
    print("Good Morning Sir! ")
if(hour >= 12 and hour < 17):
    print("Good Afternoon Sir! ")
if(hour >= 17 and hour < 0):
    print("Good Night Sir! ")

