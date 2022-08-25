import os
import time
def clear():
    command = 'clear'
    if os.name in ('nt', 'dos'): 
        command = 'cls'
    os.system(command) 
#Changes windows clear command to clear()
#RPS V2, plays several times

#game instructions
clear()
print("\033[0;37;47m\n                                                        ")
print("\033[0;37;40m")
print("\033[0;37;40m Welcome to the rock paper scissors program.")
print()
#Player names
player_1 = input("What is the first players name: ")
player_2 = input("What is the second players name: ")
#P2 turns away and P1 makes choice
clear()
#variables
pointsp1 = 0 
pointsp2 = 0
play_Again = "Y"
while play_Again == "Y":
    print("You will be playing a game of rock paper scissors up to 5 points.")
    time.sleep(3)
    clear()
    while pointsp1 < 5 and pointsp2 < 5:
        print(f"{player_2} please turn away from the screen")
        time.sleep(3)
        print()
        print(f"\033[1;34;40m{player_1} what is your choice? (R) (P) (S)")
        p1choice = input("\033[1;37;40m")
        #P1 turn away and P2 makes choice
        clear()
        while p1choice.upper() !="R" and p1choice.upper() !="S" and p1choice.upper() !="P":
            print(f"Not a valid choice {player_1}, turn away {player_2}")
            time.sleep(3)
            print()
            p1choice = input("\033[1;34;40mWhat do you choose? (R) (P) (S): ")
            print("\033[1;37;40m")
            clear()
    
        print(f"{player_1} please turn away from the screen")
        time.sleep(3)
        print()

        print(f"\033[1;31;40m{player_2} what is your choice? (R) (P) (S)")
        p2choice = input("\033[1;37;40m")
        clear()
        while p2choice.upper() !="R" and p2choice.upper() !="S" and p2choice.upper() !="P":
            print(f"Not a valid choice {player_2}, turn away {player_1}")
            time.sleep(3)
            print()
            p2choice = input("\033[1;31;40mWhat do you choose? (R) (P) (S): ")
            print("\033[1;37;40m")
        #Report player choices
        clear()
        print(f"\033[1;34;40m{player_1} picked {p1choice}")
        print(f"\033[1;31;40m{player_2} picked {p2choice}")
        print(f"\033[1;37;40m")
        #Game engine responds back to players
        if p1choice.upper() == "R":
            if p2choice.upper() == "R":
                print(f"Tie game")
            elif p2choice.upper() == "P":
                print(f"{player_2} wins.")
                pointsp2 = pointsp2 + 1
            elif p2choice.upper() == "S":
                print(f"{player_1} wins")
                pointsp1 = pointsp1 + 1
        elif p1choice.upper() == "P":
            if p2choice.upper() == "P":
                print(f"Tie game")
            elif p2choice.upper() == "S":
                print(f"{player_2} wins.")
                pointsp2 = pointsp2 + 1
            elif p2choice.upper == "R":
                print(f"{player_1} wins")
                pointsp1 = pointsp1 + 1
        elif p1choice.upper() == "S":
            if p2choice.upper() == "S":
                print(f"Tie game")
            elif p2choice.upper() == "R":
                print(f"{player_2} wins.")
                pointsp2 = pointsp2 + 1
            elif p2choice.upper() == "P":
                print(f"{player_1} wins")
                pointsp1 = pointsp1 + 1
        print(f"{player_1} has {pointsp1} point(s), {player_2} has {pointsp2} point(s).")
        print()
        input("Input anything to continue ")
        clear()
    #winning messages
    if pointsp1 >= 5:
        clear()
        print(f"Congratulations {player_1} you won, going {pointsp1}-{pointsp2}")
    elif pointsp2 >= 5:
            clear()
            print(f"Congratulations {player_2} you won, going {pointsp2}-{pointsp1}")
    print()
    print("Do you wish to play again (Y) (N)")
    play_Again = input()
    #data validation
    while play_Again.upper() != "Y" and play_Again.upper() != "N":
        print("Invalid Input")
        print("Do you want to play again (Y) (N)")
        play_Again = input("")
        clear()
    play_Again = play_Again.upper()
    if play_Again.upper() == "Y":
        pointsp1 = 0
        pointsp2 = 0
        clear()
    else:
        pass


clear()
print("Thank you for playing")
print()
print("Program shutting down....")
print("\033[0;37;47m\n                                                        ")
print("\033[0;37;40m")