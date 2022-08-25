import time,random,os
#variables
play_again = True
die = [""]*4
approvedboolean = ["Y"],["N"],["y"],["n"]
saveddie = 0
savednum = 0
won = False
turn = 0
d1 = "x"
d2 = "x"
d3 = "x"
#definitions
def ogrole():
    global die,d1,d2,d3
    if d1 != "dnr":
        die[1] = random.randint(1,6)
    if d2!= "dnr":
        die[2] = random.randint(1,6)
    if d3 != "dnr":
        die[3] = random.randint(1,6)
    d1 = "x"
    d2 = "x"
    d3 = "x"
    #rolling system, clears previous saves
def playerchoice():
    global savednum
    global die
    global turn
    global d1,d2,d3
    print(f"You rolled a {die[1]}, {die[2]}, and a {die[3]}.")
    print("What number do you wish to save")
    user_input = input()
    str(user_input)
    while user_input != "1" and user_input != "2" and user_input != "3" and user_input != "4" and user_input != "5" and user_input != "6":
        #input validation
        print("Invalid Input.")
        print("What number do you wish to save")
        user_input = input()
        if user_input == "1" or user_input == "2" or user_input == "3" or user_input == "4" or user_input == "5" or user_input == "6":
            break
    user_input = int(user_input)
    #determines what to not role
    if user_input in die:
        if user_input == die[1]:
            d1 = "dnr"
        if user_input == die[2]:
            d2 = "dnr"
        if user_input == die[3]:
            d3 = "dnr"
    
def checkwin():
    global turn,won
    turn = turn+1
    if die[1] == die[2] and die[2] == die[3]:
        print()
        print("Congrats, you win!")
        print()
        won == True
    if turn>=3:
        print()
        print("You lost!")
        print()
        won = True
    #simple lose and win system
        
#main code
while play_again:
    print("————————————————————————————————————————")
    print("Welcome to Speed Yahtzee!")
    print()
    print("You will have 3 tries to get a Yahtzee.")
    print("You can choose to save all die of a certain number.")
    print("If you get 3 of the same within the 3 rolls, you win.")
    print("If you do not get that, you lose.")
    print("————————————————————————————————————————")
    print()
    input("Enter To Continue")
    while won == False:
        ogrole()
        checkwin()
        if won == True:
            break #makes it so that if the player wins it breaks the loop
        playerchoice()
    
    print("Do you want to play again? (Y) (N)")
    playinp = input()
    if playinp == "Y":
        pass
        won = False
    if playinp == "N":
        break
