#input validation procerss

#range validation

user_Input = int(input("Please type in a number between 1 and 10: "))
# data validation
while user_Input < 1 or user_Input > 10:
    print("Invalid number")
    user_Input = int(input("Please type in a number between 1 and 10: "))


#Input check
user_Input = input("Do you want to play again? (Y) (N): ")
#data validation
while user_Input.upper() != "Y" and user_Input.upper() != "N":
    print("Invalid Input")
    user_Input = input("Do you want to play again? (Y) (N): ")


#multiple input checks
user_Input = input("What do you choose? (R) (P) (S): ")
#data validation
while user_Input.upper() !="R" and user_Input.upper() !="S" and user_Input.upper() !="S":
    print("Not a valid choice")
    user_Input = input("What do you choose? (R) (P) (S): ")
    '''
#RPS V2


#variables
p1_Score = 0
p2_Score = 0
play_Again = True

##WELCOME AND INSTRUCTIONS
print(f"")
#playernames

#play again loop
while play_Again == True:
    
    #scroes less then 5? Game loop
    while p1_Score < 5 and p2_Score <5:
            
        #p1 choice

        #p2 choice

        #check for winner
        player2choice = "a"
        if play2Choice.lower() == "r":
        #scoreboard
    #end of game
    if p1_Score == 5:
        print("Congrats player 1 wins")
    else:
        print("Congrats player 2 wins")
    #do you wanna play again?
    user_Input = input("Would you like to play again? (Y) (N): ")
    #data val

    if user_Input.upper() == "N":
        play_Again == False
    else:
        play_Again == True
        p1_Score = 0
        p2_Score = 0
        



print("Thanks for playing")
print("Program will now exit")
'''