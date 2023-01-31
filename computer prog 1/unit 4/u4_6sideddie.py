import random, os
die1 = "  ____ \n |    | \n | O  | \n |    | \n  ————"
die2 = "  ____ \n |O   | \n |    | \n |   O| \n  ————"
die3 = "  ____ \n |O   | \n | O  | \n |   O| \n  ————"
die4 = "  ____ \n |O  O| \n |    | \n |O  O| \n  ————"
die5 = "  ____ \n |O  O| \n | O  | \n |O  O| \n  ————"
die6 = "  ____ \n |O  O| \n |O  O| \n |O  O| \n  ————"
dielist = [die1,die2,die3,die4,die5,die6]
roll_Again = True
print("—————————Welcome to the Dice program—————————")
print()
print("This program will roll a standard 6 sided die, generating a number 1-6.")
input("Enter to roll die")
while roll_Again == True:
    print(f"{dielist[random.randint(1,5)]}")
    print("Do you wish to play again? (Y) (N)")
    user_Input = input()
    while user_Input.upper() != "Y" and user_Input.upper() != "N":
        print("Invalid input")
        print("Do you wish to play again? (Y) (N)")
        user_Input = input()
    if user_Input.upper() == "Y":
        os.system("cls")
    if user_Input.upper() == "N":
        roll_Again = False