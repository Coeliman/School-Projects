#intro
print("This is a calculator to determine what grade you are in high school based on your age.")
print()
#Get age and set to integer
age = int(input("How old are you: "))
#else ifs to figure out what grade they are
if age < 15:
    print("You are not in high school yet.")
elif age == 15:
    print("You are a freshman, welcome to high school.")
elif age == 16:
    print("You are a sophmore, almost half way through.")
elif age == 17:
    print("You are a junior, you are past the half way mark.")
elif age == 18:
    print("You are a senior, get ready to graduate this year.")
else:
    print("You are out of high school and have graduated from it.")
