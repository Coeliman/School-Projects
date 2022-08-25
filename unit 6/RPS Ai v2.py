import random,os
#vars
play_Again = True
playerchoice = " "
botchoice = " "
playerpoints = "0"
botpoints = "0"
playerpoints = int(playerpoints)
botpoints = int(botpoints)
algor = ["","",""]
userchoices = []
choicescount = []
print("Welcome to bot rock paper scisscors.")
print("You will be playing against a that chooses based on machine learning..")
input("Enter to continue.")
while play_Again == True:
    playerchoice = input("What do you choose? (R) (P) (S) ")
    while playerchoice.upper() !="R" and playerchoice.upper() !="S" and playerchoice.upper() !="P":
        print("Invalid input.")
        playerchoice = input("What do you choose? (R) (P) (S) ")
    playerchoice = playerchoice.upper()
    userchoices.append(playerchoice)
    choicescount = len(userchoices)
    os.system("cls")
    asf = random.randint(1,3)
    Rvar = userchoices.count("R")
    Pvar = userchoices.count("P")
    Svar = userchoices.count("S")
    algor[0] = (Rvar/choicescount)*100
    algor[1] = (Pvar/choicescount)*100
    algor[2] = (Svar/choicescount)*100
    compChoice = random.randint(1,100)
    if compChoice < algor[0]:
        botchoice = "P"
    elif compChoice > algor[0] and compChoice < (algor[0]+algor[1]):
        botchoice = "S"
    else:
        botchoice = "P"
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