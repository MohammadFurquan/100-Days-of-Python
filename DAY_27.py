# EXERCISE
# Create a program capable of displaying questions to the user like KBC.
# Use List data type to store the questions and their correct answers
# Display the final amount the person is taking home after playing the game.


ques = ["1. What is Python","2. Is Html Programming Language","3. Is there operator Loading in Java"]
ans = ["Language","No","Yes","No it is not in Java"]
print("'WELCOME TO KBC'")
for i in range(len(ques)):
    print(ques[i])
    user_answer = 0
    for j in range(len(ans)):
        print(ans[j])
        break
    
    user_answer = int(input("Enter Answer as Index no : "))
    if user_answer == j:
        print("Congratulatiosn Correct")
    else:
        print("Well Tried")


