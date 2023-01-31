

import turtle,os
cardstaken = 0
bob = turtle.Turtle()
bob.speed(0)
def card(color):
	bob.color(color)
	bob.fillcolor(color)
	bob.begin_fill()
	for i in range(2):
		bob.forward(15)
		bob.left(90)
		bob.forward(30)
		bob.left(90)
	bob.end_fill()
	bob.penup()
	bob.forward(30)
	bob.pendown()
def setup():
	bob.penup()
	bob.goto(-300,0)
	bob.pendown()
	for i in range(21):
		card("black")
	bob.penup()
	bob.goto(-300,0)
	bob.pendown()
def turn(player):
	global cardstaken
	os.system('clear')
	print("How many cards would you like to take Player"+ str(player))
	UI = input()
	if UI.isnumeric():
		if int(UI) == 3:
			cardstaken = cardstaken + 3
			for i in range(3):
				card("red")
		elif int(UI) == 2:
			cardstaken = cardstaken +2
			for i in range(2):
				card("red")
		elif int(UI) == 1:
			cardstaken = cardstaken + 1
			card("red")
		else:
			print("Error1")
	else:
		print("error2")
def checkwin(player):
	global win
	if cardstaken <= 21:
		if player == 1:
			os.system('clear')
			print("Player 2 won!")
			win = True
		else:
			os.system('clear')
			print("Player 1 won!")
			win = True
	else:
		pass
while True:
	setup()
	while True:
		turn(1)
		checkwin(1)
		if win == True:
			break
		turn(2)
		checkwin(2)
		if win == True:
			break
	print("Play again?")
	UI = input()
	if UI == "Y":
		cardstaken = 0
		pass
	else:
		break