#unit 4 practice file

#sleepo practice
import time
import random
'''
print("muy segundo es")
time.sleep(5)
print(random.randint(0,69))

anime_list = ["dogman","obama","tiger","mrclean","michaelangelo"]
print(anime_list)
print(anime_list[random.randint(0,4)])

#apponding
user_Input = input("worst anime? ")
anime_list.append(user_Input)
print(anime_list)


#data val
approved_Inputs = ["YES","NO","Y","N"]
user_Input = input("Do you wanna play again? Y N")
while user_Input.upper() not in approved_Inputs:
    print("Invalid input")
    user_input = input("Do you wanna play again? Y N")
    
anime_list.sort()
'''

student_names = []
num = int(input("How many students exist? "))

for i in range(num):
    user_Input = input("Student name: ")
    student_names.append(user_Input)

print(student_names)

student_names.sort()
print(student_names)

print(f"My favorite student is: {random.choice(student_names)}")



