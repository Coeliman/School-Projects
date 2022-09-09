#import
import random, os
#variables
approved_Inputs = ["Y","N"]
roll_Again = True
dice = [" "] * 9 
#custom
def draw_Dice():
    print(" ______")
    print(f"|{dice[0]} {dice[1]} {dice[2]}|")
    print(f"|{dice[3]} {dice[4]} {dice[5]}|")
    print(f"|{dice[6]} {dice[7]} {dice[8]}|")
    print(" ——————")
def roll_Dice():
    dice_Number = random.randint(1,6)
    global dice
    if dice_Number == 1:
        dice[4] = "O"
    elif dice_Number == 2:
        dice[0] = "O"
        dice[8] = "O"
    elif dice_Number == 3:
        dice[2] = "O"
        dice[6] = "O"
        dice[4] = "O"
    elif dice_Number == 4:
        dice[0] = "O"
        dice[2] = "O"
        dice[6] = "O"
        dice[8] = "O"
    elif dice_Number == 5:
        dice[0] = "O"
        dice[2] = "O"
        dice[6] = "O"
        dice[8] = "O"
        dice[4] = "O"
    elif dice_Number == 6:
        dice[0] = "O"
        dice[2] = "O"
        dice[6] = "O"
        dice[8] = "O"
        dice[7] = "O"
        dice[1] = "O"
#main prog
print("This program will roll a standard 6 sided die, generating a number 1-6.")
input("Enter to roll die")
while roll_Again == True:
    roll_Dice()
    draw_Dice()
    print("Do you want to roll again? (Y) (N) ")
    user_Input = input()
    while user_Input.upper() not in approved_Inputs:
        print("Invlaid input")
        print("Do you want to roll again? (Y) (N) ")
        user_Input = input()
    if user_Input.upper() == "Y":
        dice [0] = " "
        dice [1] = " "
        dice [2] = " "
        dice [3] = " "
        dice [4] = " "
        dice [5] = " "
        dice [6] = " "
        dice [7] = " "
        dice [8] = " "
        os.system("cls")
    if user_Input.upper() == "N":
        roll_Again = False