#2 player tic tac toe
#imports
import os,random
#vars
approved_Inputs = ["Y","N"]
player_1 = " "
player_2 = " "
choice = [" "] * 10
choice = ["-",1,2,3,4,5,6,7,8,9]
play_Again = True
p1_Move = 0
bot_Move = 0
is_Winner = False
wse = ""
bwc = ""
#defs
def p1_Turn(): #this command just gives the location to where to put stuff
    print(f"{player_1}'s turn. Where would you like to play?")
    p1_Move = int(input())
    while p1_Move >=10 or p1_Move <=0:
        print("Invalid move")
        print(f"{player_1}'s turn. Where would you like to play?")
        p1_Move = int(input()) 
    CheckMove(p1_Move,"X")
def bot_Turn(): 
    bot_Move = 0
    #priority 1 (try to win)
    #sides to sides
    has_played = False
    if has_played == False:
        if choice[1] == "O" and choice [2] == "O" and choice[3] == " ":
            bot_Move = 3
        elif choice[2] == "O" and choice [3] == "O" and choice[1] == " ":
            bot_Move = 1
        elif choice[1] == "O" and choice [3] == "O" and choice[2] == " ":
            bot_Move = 2
        elif choice[4] == "O" and choice [5] == "O" and choice[6] == " ":
            bot_Move = 6
        elif choice[5] == "O" and choice [6] == "O" and choice[4] == " ":
            bot_Move = 4
        elif choice[4] == "O" and choice [6] == "O" and choice[4] == " ":
            bot_Move = 5
        elif choice[7] == "O" and choice [8] == "O" and choice[9] == " ":
            bot_Move = 9
        elif choice[7] == "O" and choice [9] == "O" and choice[8] == " ":
            bot_Move = 8
        elif choice[8] == "O" and choice [9] == "O" and choice[7] == " ":
            bot_Move = 7
            #up and down
        elif choice[1] == "O" and choice [4] == "O" and choice[7] == " ":
            bot_Move = 7
        elif choice[4] == "O" and choice [7] == "O" and choice[1] == " ":
            bot_Move = 1
        elif choice[7] == "O" and choice [1] == "O" and choice[4] == " ":
            bot_Move = 4
        elif choice[2] == "O" and choice [5] == "O" and choice[8] == " ":
            bot_Move = 8
        elif choice[2] == "O" and choice [8] == "O" and choice[5] == " ":
            bot_Move = 5
        elif choice[8] == "O" and choice [5] == "O" and choice[2] == " ":
            bot_Move = 2
        elif choice[3] == "O" and choice [6] == "O" and choice[9] == " ":
            bot_Move = 3
        elif choice[6] == "O" and choice [9] == "O" and choice[3] == " ":
            bot_Move = 6
        elif choice[3] == "O" and choice [9] == "O" and choice[6] == " ":
            bot_Move = 3
            #diagonal
        elif choice[1] == "O" and choice [5] == "O" and choice[9] == " ":
            bot_Move = 1
        elif choice[5] == "O" and choice [9] == "O" and choice[1] == " ":
            bot_Move = 5
        elif choice[9] == "O" and choice [1] == "O" and choice[5] == " ":
            bot_Move = 9
        elif choice[3] == "O" and choice [5] == "O" and choice[7] == " ":
            bot_Move = 2
        elif choice[5] == "O" and choice [7] == "O" and choice[3] == " ":
            bot_Move = 5
        elif choice[3] == "O" and choice [7] == "O" and choice[5] == " ":
            bot_Move = 2
        if bot_Move != 0:
            has_played = True
    #priority 2 (Block Player)
    if has_played == False:
        if choice[1] == "X" and choice [2] == "X" and choice[3] == " ":
            bot_Move = 3
        elif choice[2] == "X" and choice [3] == "X" and choice[1] == " ":
            bot_Move = 1
        elif choice[1] == "X" and choice [3] == "X" and choice[2] == " ":
            bot_Move = 2
        elif choice[4] == "X" and choice [5] == "X" and choice[6] == " ":
            bot_Move = 6
        elif choice[5] == "X" and choice [6] == "X" and choice[4] == " ":
            bot_Move = 4
        elif choice[4] == "X" and choice [6] == "X" and choice[4] == " ":
            bot_Move = 5
        elif choice[7] == "X" and choice [8] == "X" and choice[9] == " ":
            bot_Move = 9
        elif choice[7] == "X" and choice [9] == "X" and choice[8] == " ":
            bot_Move = 8
        elif choice[8] == "X" and choice [9] == "X" and choice[7] == " ":
            bot_Move = 7
            #up and down
        elif choice[1] == "X" and choice [4] == "X" and choice[7] == " ":
            bot_Move = 7
        elif choice[4] == "X" and choice [7] == "X" and choice[1] == " ":
            bot_Move = 1
        elif choice[7] == "X" and choice [1] == "X" and choice[4] == " ":
            bot_Move = 4
        elif choice[2] == "X" and choice [5] == "X" and choice[8] == " ":
            bot_Move = 8
        elif choice[2] == "X" and choice [8] == "X" and choice[5] == " ":
            bot_Move = 5
        elif choice[8] == "X" and choice [5] == "X" and choice[2] == " ":
            bot_Move = 2
        elif choice[3] == "X" and choice [6] == "X" and choice[9] == " ":
            bot_Move = 3
        elif choice[6] == "X" and choice [9] == "X" and choice[3] == " ":
            bot_Move = 6
        elif choice[3] == "X" and choice [9] == "X" and choice[6] == " ":
            bot_Move = 3
            #diagonal
        elif choice[1] == "X" and choice [5] == "X" and choice[9] == " ":
            bot_Move = 1
        elif choice[5] == "X" and choice [9] == "X" and choice[1] == " ":
            bot_Move = 5
        elif choice[9] == "X" and choice [1] == "X" and choice[5] == " ":
            bot_Move = 9
        elif choice[2] == "X" and choice [5] == "X" and choice[7] == " ":
            bot_Move = 2
        elif choice[5] == "X" and choice [7] == "X" and choice[2] == " ":
            bot_Move = 5
        elif choice[2] == "X" and choice [7] == "X" and choice[5] == " ":
            bot_Move = 2
        if bot_Move != 0:
            has_played = True 
    #priority 3 (prevent "cheese" setup)
    if has_played == False:
        if choice[1] == "X" and choice[9] == " ":
            bot_Move = 9
        elif choice[9] == "X" and choice[1] == " ":
            bot_Move = 1
        elif choice[3] == "X" and choice[7] == " ":
            bot_Move = 7 
        elif choice[7] == "X" and choice[3] == " ":
            bot_Move = 3
        if bot_Move != 0:
            has_played = True
    #priority 4 (middle)
    if has_played == False:
        if choice[5] == " ":
            bot_Move = 5
        if bot_Move != 0:
            has_played = True
    #priority 5 (random)
    if has_played == False:
        asd = random.randint(1,9)
        while choice[asd] != " ":
            asd = random.randint(1,9)
        bot_Move = asd
    CheckMove(bot_Move,"O") 
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
            print("ERROR, SHOULD NOT HAPPEN")
            input()
def CheckWinner():
    global wse
    #horizontal checks
    if choice[7] == choice[8] and choice[8] == choice[9] and choice[7] != " ":
        wse = choice[7]
    elif choice[4] == choice[5] and choice[5] == choice[6] and choice[4] != " ":
        wse = choice[4]
    elif choice[1] == choice[2] and choice[2] == choice[3] and choice[1] != " ":
        wse =  choice[1]
    #vertical checks
    if choice[1] == choice[4] and choice[4] == choice[7] and choice[1] != " ":
        wse = choice[1]
    elif choice[2] == choice[5] and choice[5] == choice[8] and choice[2] != " ":
        wse = choice[2]
    elif choice[3] == choice[6] and choice[6] == choice[9] and choice[3] != " ":
        wse = choice[3]
    #diagonal checks
    if choice[1] == choice[5] and choice[5] == choice[9] and choice[1] != " ":
        wse = choice[1]
    elif choice[3] == choice[5] and choice[5] == choice[7] and choice[3] != " ":
        wse =  choice[3]
    if choice[1] != " " and choice[2] != " " and  choice[3] != " " and  choice[4] != " " and  choice[5] != " " and  choice[6] != " " and  choice[7] != " " and  choice[8] != " " and  choice[9] != " ":
        wse = choice[0]

#Program
print("This is a simple Tic-Tac-Toe program where you play against a bot!.")
print()
player_1 = input("Who is player 1 (X)? ")
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
        abc = random.randint(1,2)
        while abc == 1:
            os.system("cls")
            drawBoard()
            p1_Turn()
            CheckWinner()
            if wse == "X":
                os.system("cls")
                drawBoard()
                print(f"{player_1} wins!!!")
                bbreak = True
                break
            elif wse == "-":
                os.system("cls")
                drawBoard()
                print("Tie game")
                bbreak = True
                break
            os.system("cls")
            drawBoard()
            bot_Turn()
            CheckWinner()
            if wse == "O":
                os.system("cls")
                drawBoard()
                print(f"Bot wins!!!")
                bbreak = True
                break
            elif wse == "-":
                os.system("cls")
                drawBoard()
                print("Tie game")
                bbreak = True
                break
            os.system("cls")
        while abc == 2:
            os.system("cls")
            drawBoard()
            bot_Turn()
            CheckWinner()
            if wse == "O":
                os.system("cls")
                drawBoard()
                print(f"Bot wins!!!")
                bbreak = True
                bbreak = True
                break
            elif wse == "-":
                os.system("cls")
                drawBoard()
                print("Tie game")
                bbreak = True
                break
            os.system("cls")
            drawBoard()
            p1_Turn()
            CheckWinner()
            if wse == "X":
                os.system("cls")
                drawBoard()
                print(f"{player_1} wins!!!")
                bbreak = True
                break
            elif wse == "-":
                os.system("cls")
                drawBoard()
                print("Tie game")
                bbreak = True
                break
            os.system("cls")
        if bbreak == True:
            break

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
        wse = ""
        bwc = ""
        p1_Move = 0
        bot_move = 0
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
        
