import turtle
sam = turtle.Turtle()
#pensize 15 works best
#draws olymp rings
sam.pensize(15)
sam.penup()
sam.goto(-275,-10)
sam.pendown()
sam.color("blue")
sam.circle(100) #blue ring
sam.penup()
sam.color("yellow")
sam.goto(-150,-120)
sam.pendown()
sam.circle(100) #yellow ring
sam.penup()
sam.goto(-25,-10)
sam.color("black")
sam.pendown()
sam.circle(100) #black ring
sam.penup()
sam.color("green")
sam.goto(100,-120) 
sam.pendown()
sam.circle(100) #green ring
sam.penup()
sam.color("red")
sam.goto(225,-10)
sam.pendown()
sam.circle(100) #red ring
input()