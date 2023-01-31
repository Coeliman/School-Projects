#2 player tic tac toe
#imports
import os
#vars
approved_Inputs = ["Y","N"]
player_1 = " "
player_2 = " "
choice = [" "] * 10
choice[0] = "-"
choice[1] = 1
choice[2] = 2
choice[3] = 3
choice[4] = 4
choice[5] = 5
choice[6] = 6
choice[7] = 7 
choice[8] = 8
choice[9] = 9
play_Again = True
p1_Move = 0
p2_Move = 0
is_Winner = False
#defs
def p1_Turn(): #this command just gives the location to where to put stuff
    print(f"{player_1}'s turn. Where would you like to play?")
    p1_Move = int(input())
    while p1_Move >=10 or p1_Move <=0:
        print("Invalid move")
        print(f"{player_1}'s turn. Where would you like to play?")
        p1_Move = int(input()) 
    CheckMove(p1_Move,"X")
def p2_Turn(): #this command just gives the location to where to put stuff
    print(f"{player_2}'s turn. Where would you like to play?")
    p2_Move = int(input())
    while p2_Move >=10 or p2_Move <=0:
        print("Invalid move")
        print(f"{player_2}'s turn. Where would you like to play?")
        p2_Move = int(input()) 
    CheckMove(p2_Move,"O") 
def drawBoard(): #draws board
    print(f"   {choice[1]}   |   {choice[2]}   |   {choice[3]}   ")
    print(" ————————————————————— ")
    print(f"   {choice[4]}   |   {choice[5]}   |   {choice[6]}   ")
    print(" ————————————————————— ")
    print(f"   {choice[7]}   |   {choice[8]}   |   {choice[9]}   ")
def CheckMove(move,symbol):
    if choice[move] == " ":
        choice[move] = symbol
        drawBoard()
    else:
        print("That spot is already taken, try again")
        if symbol == "X":
            p1_Turn()
        else:
            p2_Turn()
def CheckWinner():
    #horizontal checks
    if choice[7] == choice[8] and choice[8] == choice[9] and choice[7] != " ":
        return choice[7]
    elif choice[4] == choice[5] and choice[5] == choice[6] and choice[4] != " ":
        return choice[4]
    elif choice[1] == choice[2] and choice[2] == choice[3] and choice[1] != " ":
        return choice[1]
    #vertical checks
    if choice[1] == choice[4] and choice[4] == choice[7] and choice[1] != " ":
        return choice[1]
    elif choice[2] == choice[5] and choice[5] == choice[8] and choice[2] != " ":
        return choice[2]
    elif choice[3] == choice[6] and choice[6] == choice[9] and choice[3] != " ":
        return choice[3]
    #diagonal checks
    if choice[1] == choice[5] and choice[5] == choice[9] and choice[1] != " ":
        return choice[1]
    elif choice[3] == choice[5] and choice[5] == choice[7] and choice[3] != " ":
        return choice[3]
    if choice[1] != " " and choice[2] != " " and  choice[3] != " " and  choice[4] != " " and  choice[5] != " " and  choice[6] != " " and  choice[7] != " " and  choice[8] != " " and  choice[9] != " ":
        return choice[0]

#Program
print("This is a simple Tic-Tac-Toe program where you can play Tic-Tac-Toe with one friend.")
print()
player_1 = input("Who is player 1 (X)? ")
player_2 = input("Who is player 2 (O)? ")
os.system("cls")
drawBoard()
print()
print("These numbers coorolate to board spots.")
print("Type in the number of the spot you wish to put your symbol.")
input("Enter to continue ")
choice[1] = " "
choice[2] = " "
choice[3] = " "
choice[4] = " "
choice[5] = " "
choice[6] = " "
choice[7] = " "
choice[8] = " "
choice[9] = " "
os.system("cls")
while play_Again == True:
    while is_Winner == False:
        os.system("cls")
        drawBoard()
        p1_Turn()
        if CheckWinner() == "X":
            os.system("cls")
            drawBoard()
            print(f"{player_1} wins!!!")
            break
        elif CheckWinner() == "-":
            os.system("cls")
            drawBoard()
            print("Tie game")
            break
        os.system("cls")
        drawBoard()
        p2_Turn()
        if CheckWinner() == "Y":
            os.system("cls")
            drawBoard()
            print(f"{player_2} wins!!!")
            break
        elif CheckWinner() == "-":
            os.system("cls")
            drawBoard()
            print("Tie game")
            break
        os.system("cls")
    print()
    print("Game over, would you like to play again (Y) (N)")
    play_Again = input()
    while play_Again.upper() not in approved_Inputs:
        print("Invalid Input")
        print("Game over, would you like to play again (Y) (N)")
        play_Again = input()
    if play_Again.upper() == "Y":
        play_Again = True
        is_Winner = False
        os.system("cls")
        choice[1] = 1
        choice[2] = 2
        choice[3] = 3
        choice[4] = 4
        choice[5] = 5
        choice[6] = 6
        choice[7] = 7 
        choice[8] = 8
        choice[9] = 9
        drawBoard()
        print()
        print("These numbers coorolate to board spots.")
        print("Type in the number of the spot you wish to put your symbol.")
        input("Enter to continue ")
        os.system("cls")
        choice[1] = " "
        choice[2] = " "
        choice[3] = " "
        choice[4] = " "
        choice[5] = " "
        choice[6] = " "
        choice[7] = " "
        choice[8] = " "
        choice[9] = " "
