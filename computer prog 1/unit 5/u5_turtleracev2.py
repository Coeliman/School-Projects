import turtle
import random
import os
'''
while name.xcor() < 300 and blue.xcor() < 300
    red.forward(random.randint)
    blue.forward(random.randint)
if red.xcor() >= 300 
    print("Red wins")
draw.write("Start"
'''
draw = turtle.Turtle()
scores = turtle.Turtle()
scores.penup()
scores.goto(1000,1000)
#map
draw.speed(100)
draw.penup()
draw.goto(-300,150)
draw.pendown()
draw.right(90)
draw.forward(300)
draw.left(90)
draw.forward(600)
draw.left(90)
draw.forward(300)
draw.left(90)
draw.forward(600)
draw.left(90)
draw.forward(75)
draw.left(90)
draw.forward(600)
draw.right(90)
draw.forward(75)
draw.right(90)
draw.forward(600)
draw.left(90)
draw.forward(75)
draw.left(90)
draw.forward(600)
draw.penup()
draw.goto(-300, -200)
draw.write("Start", font=('Arial','30'))
draw.penup()
draw.goto(230,-200)
draw.pendown()
draw.write("End", font=('Arial','30'))
draw.penup()
draw.goto(-500,-500)
#makes scoreboard
scoreboard = turtle.Turtle()
scoreboard.penup()
scoreboard.goto(-400,300)
scoreboard.pendown()
scoreboard.forward(800)
scoreboard.penup()
scoreboard.goto(-100,325)
scoreboard.pendown()
scoreboard.write("Scoreboard", font=('Arial','30'))
scoreboard.penup()
scoreboard.goto(-300,300)
scoreboard.pendown()
scoreboard.write("Red")
scoreboard.penup()
scoreboard.goto(-100,300)
scoreboard.pendown()
scoreboard.write("Blue")
scoreboard.penup()
scoreboard.goto(100,300)
scoreboard.pendown()
scoreboard.write("Green")
scoreboard.penup()
scoreboard.goto(300,300)
scoreboard.pendown()
scoreboard.write("Yellow")
scoreboard.penup()
scoreboard.goto(1000,1000)
#makes turtles
red = turtle.Turtle()
green = turtle.Turtle()
blue = turtle.Turtle()
yellow = turtle.Turtle()
red.penup()
green.penup()
blue.penup()
yellow.penup()
red.goto(-300,112.5)
green.goto(-300,37.5)
blue.goto(-300,-37.5)
yellow.goto(-300,-112.5)
red.color("red")
green.color("green")
blue.color("blue")
yellow.color("orange")
red.pendown()
green.pendown()
blue.pendown()
yellow.pendown()
#actual race
race = "Y"
redscore = 0
bluescore = 0
greenscore = 0
yellowscore = 0
winscore = int(input("What score to win? "))
while redscore != winscore and bluescore != winscore and greenscore != winscore and yellowscore != winscore and race == "Y":
    print(f"Going to {winscore}")
    input("——————Enter to Begin——————")
    redint = random.randint(1,4)
    blueint = random.randint(1,4)
    greenint = random.randint(1,4)
    yellowint = random.randint(1,4)
    while red.xcor() < 300 and blue.xcor() < 300 and green.xcor() < 300 and yellow.xcor() < 300:
        intr = random.randint(-5,5)
        intb = random.randint(-5,5)
        intg = random.randint(-5,5)
        inty = random.randint(-5,5)
        if redint == 4:
            red.forward(3)
        else:
            red.forward(random.randint(1,5))
            red.left(intr)
        if blueint == 4:
            blue.forward(10)
            blue.left(random.randint(-20,20))
        else:
            blue.forward(random.randint(1,5))
            blue.left(intb)
        if greenint == 4:
            green.forward(random.randint(-5,10))
            green.left(intg) 
        else:
            green.forward(random.randint(1,5))
            green.left(intg)    
        if yellowint == 4:
            yellow.forward(30)
            yellow.left(random.randint(-90,90)) 
        else:
            yellow.forward(random.randint(1,5))
            yellow.left(inty)
    win = turtle.Turtle()
    win.penup()
    
    
    if red.xcor() >= 300:
        win.goto(0,-300)
        redscore = redscore+1
        win.pendown()
        win.color("red")
        win.write("Red wins!", font=('Arial','30'))
    elif blue.xcor() >= 300:
        win.goto(0,-300)
        bluescore = bluescore+1
        win.pendown()
        win.color("blue")
        win.write("Blue wins!", font=('Arial','30'))
    elif green.xcor() >= 300:
        win.goto(0,-300)
        greenscore = greenscore+1
        win.pendown()
        win.color("green")
        win.write("Green wins!", font=('Arial','30'))
    elif yellow.xcor() >= 300:
        win.goto(0,-300)
        yellowscore = yellowscore+1
        win.pendown()
        win.color("orange")
        win.write("Yellow wins!", font=('Arial','30'))
    win.penup()
    win.color("black")
    win.goto(-500,-500)
    race = input("Do you want to play again? (Y) (N)").upper()

    while race != "Y" and race !=  "N":
        print("Invalid Input")
        print()
        race = input("Do you want to play again? (Y) (N)").upper()
    if race == "Y":
        
        red.clear()
        blue.clear()
        green.clear()
        yellow.clear()
        win.clear()
        red.penup()
        blue.penup()
        green.penup()
        yellow.penup()
        red.goto(-300,112.5)
        green.goto(-300,37.5)
        blue.goto(-300,-37.5)
        yellow.goto(-300,-112.5)
        red.setheading(0)
        blue.setheading(0)
        green.setheading(0)
        yellow.setheading(0)
        red.pendown()
        blue.pendown()
        green.pendown()
        yellow.pendown()
        os.system("cls")
        #scoreboard reset
        scores.clear()
        scores.penup()
        scores.goto(-300,275)
        scores.pendown()
        scores.write(redscore)
        scores.penup()
        scores.goto(-100,275)
        scores.write(bluescore)
        scores.penup()
        scores.goto(100,275)
        scores.pendown()
        scores.write(greenscore)
        scores.penup()
        scores.goto(300,275)
        scores.pendown()
        scores.write(yellowscore)
        scores.penup()
        scores.goto(1000,1000)
        
        #continue it on and also write scores at beginning
if redscore >= winscore:
    print("Red wins")
if bluescore >= winscore:
    print("Blue wins")
if greenscore >= winscore:
    print("Green wins")
if yellowscore >= winscore:
    print("Yellow wins")
