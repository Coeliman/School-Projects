import turtle
bob =  turtle.Turtle()
y = "y"

while y == "y":
    n = int(input("How many sides: "))
    if n <= 2:
        print("Invalid input")
        n = int(input("How many sides: "))
    #caclulations
    ang = ((n-2)*180)/n
    print(ang)
    for i in range(n):
        bob.left(180-ang)
        bob.forward(50)
    y = input("Do you wish to play again? (Y) (N) ")
    if y.upper() == "Y":
        pass
    elif y.upper() == "N":
        pass
    else:
        print("Invalid input.")
        y = input("Do you wish to play again? (Y) (N) ")
