#race across the desert, get to point until caught, have different options
import random,os,time
#vars
suit_Charge = 10
thirst_Amount = 10
drink_Amount = 4
play_Again = True
player_Distance = 25
enemy_Distance = -25
has_Won = False
lose = False
#defs
def chargeSuit():
    os.system("cls")
    global suit_Charge
    suit_Charge = suit_Charge + random.randint(1,5)
    if suit_Charge > 15:
        suit_Charge = 15
        print("You are at max charge!")
        print()
    print("————————————————————————————————————————")
    print("You let your suit charge for a bit")
    print("————————————————————————————————————————")
    print("")
    input("Enter to continue")
def drinkWater():
    os.system("cls")
    global drink_Amount
    global thirst_Amount
    drink_Amount = drink_Amount - 1
    if drink_Amount > 0:
        thirst_Amount = thirst_Amount + random.randint(1,3)
        drunktaken = True
    if thirst_Amount > 10:
        thirst_Amount = 10
        print("You are at max thirst!")
        print()
    if drunktaken == True:
        print("————————————————————————————————————————")
        print("You took a sip of your water.")
        print("————————————————————————————————————————")
        print("")
        input("Enter to continue")
    elif drunktaken == False:
        print("————————————————————————————————————————")
        print("You tried drinking, but ran out of water.")
        print("————————————————————————————————————————")
        print("")
        input("Enter to continue")
def walk():
    os.system("cls")
    global player_Distance
    global suit_Charge
    move = random.randint(10,20)
    player_Distance = player_Distance + move
    suit_Charge = suit_Charge - random.randint(1,2)
    print("————————————————————————————————————————")
    print(f"You moved forward {move} sectors.")
    print("————————————————————————————————————————")
    print("")
    input("Enter to continue")
def run():
    os.system("cls")
    global player_Distance
    global suit_Charge
    global thirst_Amount
    move = random.randint(20,35)
    player_Distance = player_Distance + move
    suit_Charge = suit_Charge - random.randint(2,4)
    thirst_Amount = thirst_Amount - random.randint(1,2)
    print("————————————————————————————————————————")
    print(f"You moved forward {move} sectors.")
    print("————————————————————————————————————————")
    print("")
    input("Enter to continue")
def fight():
    os.system("cls")
    global enemy_Distance
    global suit_Charge
    suit_Charge = suit_Charge - random.randint(3,5)
    enemy_rand = random.randint(1,10)
    if enemy_rand == 1:
        enemy_Distance = enemy_Distance - 50
        print("————————————————————————————————————————")
        print("The enemy moved back 50 sectors.")
        print("————————————————————————————————————————")
        print("")
        input("Enter to continue")
    elif enemy_rand == 2:
        enemy_Distance = enemy_Distance - 30
        print("————————————————————————————————————————")
        print("The enemy moved back 30 sectors.")
        print("————————————————————————————————————————")
        print("")
        input("Enter to continue")
    elif enemy_rand == 3:
        enemy_Distance = enemy_Distance - 20
        print("————————————————————————————————————————")
        print("The enemy moved back 20 sectors.")
        print("————————————————————————————————————————")
        print("")
        input("Enter to continue")
    else:
        print("————————————————————————————————————————")
        print("You missed! The enemy moved back 0 sectors.")
        print("————————————————————————————————————————")
        print("")
        input("Enter to continue")
def action():
    os.system("cls")
    global actionm
    print("Action Menu")
    print()
    print("A. Drink from your water.")
    print("B. Walk ahead.")
    print("C. Run ahead.")
    print("D. Charge your suit.")
    print("E. Fight Back")
    print("F. Status Check")
    print("Q. Quit")
    print()
    print("Type the letter you would like to select.")
    userinput = input("")
    while userinput.upper() != "A" and userinput.upper() != "B" and userinput.upper() != "C" and userinput.upper() != "D" and userinput.upper() != "E" and userinput.upper() != "F" and userinput.upper() != "Q":
        print("Invalid input.")
        print("Type the letter you would like to select.")
        userinput = input("")
    actionm = userinput.upper()
def checkStats():
    os.system("cls")
    print("————————————————————————————————————————")
    print(f"Your suit charge is {suit_Charge} (15 maximum).")
    print(f"Your thirst is {thirst_Amount} (10 maximum).")
    print(f"You have {drink_Amount} drinks left.")
    print("")
    print(f"Your sector is sector {player_Distance}.")
    print(f"Your enemies sector is sector {enemy_Distance}.")
    print("————————————————————————————————————————")
    print("")
    input("Enter to continue")
    os.system("cls")
def setup():
    global suit_Charge,thirst_Amount,drink_Amount,play_Again,player_Distance,enemy_Distance,has_Won,lose
    suit_Charge = 10
    thirst_Amount = 10
    drink_Amount = 4
    play_Again = True
    player_Distance = 25
    enemy_Distance = -25
    has_Won = False
    lose = False
    os.system("cls")
    print("————————————————————Welcome to Alien Race————————————————————")
    print("")
    print("You have stolen the alien Gnarglok, their sacred artifact.")
    print("To escape the alien mothership alive you must travel 200 sectors.")
    print("You must monitor your water and charge whilst escaping.")
    print("Good luck!")
    print()
    input("Enter to continue.")
    os.system("cls")
def checkWin():
    global lose
    if suit_Charge <= 0 or thirst_Amount <= 0:
        os.system("cls")
        print("————————————————————————————————————————")
        print("You died!")
        print()
        print("You ran out of water or suit charge!")
        print("————————————————————————————————————————")
        lose = True
    elif enemy_Distance >= player_Distance:
        print("————————————————————————————————————————")
        print("You died!")
        print()
        print("The aliens caught up to you!")
        print("————————————————————————————————————————")
        lose = True
    elif player_Distance >= 200:
        print("————————————————————————————————————————")
        print("You won!")
        print()
        print("You made it to your ship with the Alien Gnarglok!")
        print("————————————————————————————————————————")
        lose = True
        
def enemyMove():
    global enemy_Distance
    yes = random.randint(1,10)
    move = random.randint(5,25)
    if yes == 10:
        enemy_Distance = enemy_Distance + 50
    else:
        enemy_Distance = enemy_Distance + move
    print()
    print("————————————————————————————————————————")
    print("The aliens moves closer.")
    print("————————————————————————————————————————")
    time.sleep(.75)
    os.system("cls")

#code
while play_Again == True:
    setup()
    while has_Won == False:
        action()
        if actionm == "A":
            drinkWater()
            enemyMove()
        elif actionm == "B":
            walk()
            enemyMove()
        elif actionm == "C":
            run()
            enemyMove()
        elif actionm == "D":
            chargeSuit()
            enemyMove()
        elif actionm == "E":
            fight()
            enemyMove()
        elif actionm == "F":
            checkStats()
        elif actionm == "Q":
            play_Again = False
            break
        checkWin()
        if lose == True:
            break
    if lose == True:
        print("Would you like to play again? (Y) (N)")
        user_Input = str(input())
        user_Input = user_Input.upper()
        while user_Input != "Y" and user_Input != "N":
            print("Invalid Input")
            print()
            print("Would you like to play again? (Y) (N)")
            user_Input = str(input())
            user_Input = user_Input.upper()
        if user_Input == "Y":
            play_Again = True
        elif user_Input == "N":
            play_Again = False
            exit()