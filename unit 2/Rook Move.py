print(f"—————This program calculates if a rook move is viable, and can be done.—————")
print()
print("What is the rooks X position:")
rookX = input("")
print("What is the rooks Y position:")
rookY = input("")
print("What X will the rook move to:")
rookmX = input("")
print("What Y will the rook move to:")
rookmY = input("")
rookmX = int(rookmX)
rookmY = int(rookmY)
rookX = int(rookX)
rookY = int(rookY)
print()
if rookX > 8:
    print("You cannot go off the board")
    exit()
else:
    pass
if rookX < 1:
    print("You cannot go off the board")
    exit()
else:
    pass

if rookY > 8:
    print("You cannot go off the board")
    exit()
else:
    pass
if rookY < 1:
    print("You cannot go off the board")
    exit()
else:
    pass

if rookmX > 8:
    print("You cannot go off the board")
    exit()
else:
    pass
if rookmX < 1:
    print("You cannot go off the board")
    exit()
else:
    pass

if rookmY > 8:
    print("You cannot go off the board")
    exit()
else:
    pass
if rookmY < 1:
    print("You cannot go off the board")
    exit()
else:
    pass

if rookX == rookmX:
    print("Valid")
    exit()
else: 
    pass
if rookY == rookmY:
    print("Valid.")
    exit()
else:
    pass
print("Invalid.")