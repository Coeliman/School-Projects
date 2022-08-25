from math import sqrt
print("This is a Right Triangle Calculator, it will calculate your right triangle")
base = int(input("What is your base: "))
height = int(input("What is your height: "))
area = 1/2*base*height
csquared = base**2 + height**2
c = sqrt(csquared)
perimeter = base+height+c
print (f"Your area is {area}")
print(f"Your perimeter is {perimeter}")