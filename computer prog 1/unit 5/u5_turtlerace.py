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

while race == "Y":
    input("——————Enter to Begin——————")
    while red.xcor() < 300 and blue.xcor() < 300 and green.xcor() < 300 and yellow.xcor() < 300:
        intr = random.randint(-5,5)
        intb = random.randint(-5,5)
        intg = random.randint(-5,5)
        inty = random.randint(-5,5)
        red.forward(random.randint(1,5))
        red.left(intr)
        blue.forward(random.randint(1,5))
        blue.left(intb)
        green.forward(random.randint(1,5))
        green.left(intg)
        yellow.forward(random.randint(1,5))
        yellow.left(inty)
    win = turtle.Turtle()
    win.penup()
    if red.xcor() >= 300:
        win.goto(0,-300)
        win.pendown()
        win.color("red")
        win.write("Red wins!", font=('Arial','30'))
    elif blue.xcor() >= 300:
        win.goto(0,-300)
        win.pendown()
        win.color("blue")
        win.write("Blue wins!", font=('Arial','30'))
    elif green.xcor() >= 300:
        win.goto(0,-300)
        win.pendown()
        win.color("green")
        win.write("Green wins!", font=('Arial','30'))
    elif yellow.xcor() >= 300:
        win.goto(0,-300)
        win.pendown()
        win.color("orange")
        win.write("Orange wins!", font=('Arial','30'))
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

