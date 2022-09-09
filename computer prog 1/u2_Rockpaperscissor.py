import os
import time
def clear():
    command = 'clear'
    if os.name in ('nt', 'dos'): 
        command = 'cls'
    os.system(command) #Changes windows clear command to clear()

#Version 1 of Rock Paper Scissors that plays through once

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
print(f"{player_2} please turn away from the screen")
time.sleep(3)
print(f"{player_1} what is your choice? (R) (P) (S)")
p1choice = input("")
#P1 turn away and P2 makes choice
clear()
print(f"{player_1} please turn away from the screen")
time.sleep(3)
print(f"{player_2} what is your choice? (R) (P) (S)")
p2choice = input("")
#Report player choices
clear()
print(f"{player_1} picked {p1choice}")
print(f"{player_2} picked {p2choice}")
#Game engine respond back to players
if p1choice.upper() == "R":
    if p2choice.upper() == "R":
        print(f"Tie game")
    elif p2choice.upper() == "P":
        print(f"{player_2} loses.")
    elif p2choice.upper == "S":
        print(f"{player_1} wins")
    else:
        print(f"Invalid choice {player_2}")
elif p1choice.upper() == "P":
    if p2choice.upper() == "P":
        print(f"Tie game")
    elif p2choice.upper() == "S":
        print(f"{player_2} loses.")
    elif p2choice.upper == "R":
        print(f"{player_1} wins")
    else:
        print(f"Invalid choice {player_2}")
elif p1choice.upper() == "S":
    if p2choice.upper() == "S":
        print(f"Tie game")
    elif p2choice.upper() == "R":
        print(f"{player_2} loses.")
    elif p2choice.upper == "P":
        print(f"{player_1} wins")
    else:
        print(f"Invalid choice {player_2}")
else:
    print(f"Invalid choice {player_1}")
    