print("Day 40: 08/10/2023")


# Write a python program to translate a message into secret code language. Use the rules below to translate normal English into Sectet Code Language

# Coding :
# if the word contains atleast 3 characters, remove the first letter and append it at the end 
#  now append three random characters at the starting and the end [harry --> mkdarryhjcd]
# else:
#      simply reverse the String


# Decoding :
# if the word conatins less than 3 characters , reverse it
# else :
#      remove 3 random characters from start and end. Now remove the last letter




x=int(input("press 1 for ENCODE or anyother number for DECODE :"))
if x == 1:  #Coding
    str = input("\nEnter the word to Code :")
    l = list(str)
    if len(str) >= 3:
        l2 = l[0]
        l = l[1:]
        l += l2
        rand = ['a', 'c', 'z']
        l += rand
        l[:0] = rand
        print("Output :",''.join(l),)
    else:
        l.reverse()
        print("Output :",''.join(l),)

#Decoding
else:
    str = input("\nEnter the word to Decode :")
    l = list(str)
    if len(str) <= 3:
        l.reverse()
        print("Output :",''.join(l),)
    else:
        l = l[3:-3]
        l2 = l.pop()
        l[:0] += l2
        print("Output :",''.join(l),)
