import random
num = random.randint(1,20)
guesses = 0
print("Guess a number 1-20, you have 4 chances.")
while guesses < 4:
    print("Guess the number: ")
    user_Input = int(input())
    while user_Input < 1 or user_Input > 20:
        print()
        print("Invalid number")
        user_Input = int(input("Guess the number: "))
    if user_Input > num:
        print()
        print("Your guess was too high")
        guesses = guesses+1
    elif user_Input < num:
        print()
        print("Your guess was too low.")
        guesses = guesses+1
    elif user_Input == num:
        print()
        print("That is the right guess!")
        break
    


if guesses < 4:    
    print(f"It tooks {guesses} guesses to get it right. Congratulations!")
elif guesses > 4:
    print(f"Nice try, but you did not guess it in 4 guesses, the right number was {num}")
elif guesses == 4:
    print(f"Nice try, but you did not guess it in 4 guesses, the right number was {num}")