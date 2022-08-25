import random
how_many_num= int(input("How many numbers would you like to have? "))
numlist = []
for i in range(how_many_num):
    numlist.append(input("What number do you want? "))

print("I will be calculating the biggest and smallest number.")
numlist.sort()
n = 0
for i in range(how_many_num):
    print(numlist[n])
    n = n+1
print(f"The smallest number is {min(numlist)} and the biggest number is  {max(numlist)}")

