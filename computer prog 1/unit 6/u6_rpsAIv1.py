import random,os
#vars
play_Again = True
playerchoice = " "
botchoice = " "
playerpoints = "0"
botpoints = "0"
playerpoints = int(playerpoints)
botpoints = int(botpoints)
print("Welcome to bot rock paper scisscors.")
print("You will be playing against a bot that chooses randomly.")
input("Enter to continue.")

while play_Again == True:
    playerchoice = input("What do you choose? (R) (P) (S) ")
    while playerchoice.upper() !="R" and playerchoice.upper() !="S" and playerchoice.upper() !="P":
        print("Invalid input.")
        playerchoice = input("What do you choose? (R) (P) (S) ")
    os.system("cls")
    asf = random.randint(1,3)
    if asf == 1:
        botchoice = "R"
    elif asf == 2:
        botchoice = "P"
    elif asf == 3:
        botchoice = "S"
    if playerchoice.upper() == "R":
        if botchoice.upper() == "R":
            print(f"Tie game")
        elif botchoice.upper() == "P":
            print(f"Bot wins.")
            botpoints = botpoints + 1
        elif botchoice.upper() == "S":
            print(f"Player wins")
            playerpoints = playerpoints + 1
    elif playerchoice.upper() == "P":
        if botchoice.upper() == "P":
            print(f"Tie game")
        elif botchoice.upper() == "S":
            print(f"Bot wins.")
            botpoints = botpoints + 1
        elif botchoice.upper == "R":
            print(f"Player wins")
            playerpoints = playerpoints + 1
    elif playerchoice.upper() == "S":
        if botchoice.upper() == "S":
            print(f"Tie game")
        elif botchoice.upper() == "R":
            print(f"Bot wins.")
            botpoints = botpoints + 1
        elif botchoice.upper() == "P":
            print(f"Player wins")
            playerpoints = playerpoints + 1
    print(f"The player has {playerpoints} points, the computer has {botpoints} points.")
    print()
    abc = input("Play again? (Y) (N)")
    while abc.upper() != "Y" and abc.upper() != "N":
        print("Invalid input.")
        abc = input("Play again? (Y) (N)")
    if abc.upper() == "Y":
        play_Again = True
        pass
    if abc.upper() == "N":
        play_Again = False
        exit()
    os.system("cls")









