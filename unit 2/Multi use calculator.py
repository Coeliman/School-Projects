#makes command since clear was not working
import os
import math

def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)

clearConsole()
#Simple calculator to help with various calculations

#Main menu
print("\033[1;34;48m ----------Welcome to our calculator----------")
print()
print("Please choose from the following options.")
print()
print("\033[1;32;48m   (A) Area Calculations")
print("\033[1;33;48m   (B) Volume Calculations")
print("\033[1;35;48m   (C) Distance Calculations")
print("\033[1;37;40m")

#Asks user for choice
user_Input = input()

#Area menu
if user_Input.upper() == "A": 
  clearConsole()
  print("\033[1;34;48m ----------Area Menu----------")
  print()
  print("Please choose from the following options.")
  print()
  print("\033[1;32;48m   (A) Octagon Calculations")
  print("\033[1;33;48m   (B) Circle Calculations")
  print("\033[1;35;48m   (C) Triangle Calculations")
  print("\033[1;37;40m")
  #User input
  user_Input = input()
  clearConsole()
  #Octagon
  if user_Input.upper() == "A":
    #show formula
    print("The formula for the area of a Octagon is 2(1+√2)a², A is a side length of the Octagon.")
    #ask for inputs
    oct_Input = input("What is your side length: ")
    oct_Input = int(oct_Input)
    #get results
    octagonArea1 = 1 + math.sqrt(2)
    octagonAreafin = 2*octagonArea1*oct_Input**2
    octagonAreafin = round(octagonAreafin, 2)
    print(f"Your octagons area is {octagonAreafin}")
    exit()
  else:
    pass
    
  #Circle
  if user_Input.upper() == "B":
    #show formula
    print("The formula for the area of a Circle is πr², R is the radius of the Circle.")
    #ask for inputs
    cir_Input = input("What is your radius: ")
    cir_Input = int(cir_Input)
    #get results
    cirAreafin = 3.14159265358979323846264338*cir_Input**2
    cirAreafin = round(cirAreafin, 2)
    print(f"Your circles area is {cirAreafin}")
    exit()
  else:
    pass

  #Triangle
  if user_Input.upper() == "C":
    #show formula
    print("The formula for a Triangles area is (b*h)/2, B is the base of a Triangle and H is the height of a Triangle.")
    #ask for inputs
    triB_Input = input("What is your base: ")
    triH_Input = input("What is your height: ")
    triH_Input = int(triH_Input)
    triB_Input = int(triB_Input)
    #get results
    b_h = triH_Input*triB_Input
    tri_Areafin = b_h/2
    tri_Areafin = round(tri_Areafin, 2)
    print(f"Your Triangles area is {tri_Areafin}")
    exit()
  else:
    pass
else:
  pass

#Volume menu
if user_Input.upper() == "B":
  clearConsole()
  print("\033[1;34;48m ----------Volume Menu----------")
  print()
  print("Please choose from the following options.")
  print()
  print("\033[1;32;48m   (A) Cylinder Calculations")
  print("\033[1;33;48m   (B) Pyramid Calculations")
  print("\033[1;35;48m   (C) Rectangular Prism Calculations")
  print("\033[1;37;40m")

  user_Input = input()
  clearConsole()
  if user_Input.upper() == "A":
    #show formula
    print("The formula for a cylinder is πr²h, R stands for the radius and H stands for the height.")
    #ask for inputs
    cylH_Input = input("What is the height of your cylinder: ")
    cylR_Input = input("What is the radius of the cylinder: ")
    #get results
    cylR_Input = int(cylR_Input)
    cylH_Input = int(cylH_Input)
    cylrsq = cylR_Input**2
    cyl_Volfin = 3.14159265358979323846264*cylrsq*cylH_Input
    cyl_Volfin = round(cyl_Volfin, 2)
    print(f"The volume of your cylinder is {cyl_Volfin}")
    exit()

  else:
    pass

  if user_Input.upper() == "B":
    #show formula
    print("The formula for the volume of a pyramid is lwh/3, L is length W is width H is height.")
    #ask for inputs
    pyrL_Input = int(input("What is the length of the pyramid: "))
    pyrW_Input = int(input("What is the width of the pyramid: "))
    pyrH_Input = int(input("What is the height of the pyramid: "))
    #get results
    pyrCom = pyrL_Input*pyrW_Input*pyrH_Input
    pyr_Volfin = pyrCom/3
    pyr_Volfin = round(pyr_Volfin, 2)
    print(f"The volume of your pyramid is {pyr_Volfin}")
    exit()
  else:
    pass
  
  if user_Input.upper() == "C":
    #show formula
    print("The formula for the volume of a rectangular prism is whl, W is width, H is height, L is length.")
    #ask for inputs
    recW_Input = int(input("What is your width: "))
    recH_Input = int(input("What is your height: "))
    recL_Input = int(input("What is your length: "))
    #get results
    rec_Volfin = recW_Input*recH_Input*recL_Input
    rec_Volfin = round(rec_Volfin)
    print(f"The volume of the rectangular prism is {rec_Volfin}")
    exit()
  else:
    pass
else:
  pass

if user_Input.upper() == "C": 
  clearConsole()
  print("\033[1;34;48m ----------Distance Menu----------")
  print()
  print("Please choose from the following options.")
  print()
  print("\033[1;32;48m   (A) Distance Formula")
  print("\033[1;33;48m   (B) Meters to feet")
  print("\033[1;35;48m   (C) Kilometers to miles")
  print("\033[1;37;40m")
  #User input
  user_Input = input()
  clearConsole()

  if user_Input.upper() == "A":
    #show formula
    print("The distance formula is squareroot((x2-x1)²+(y2-y1)², x1 and y1 are your first coordinates, and x2 and y2 are your second.")
    #ask for inputs
    disx1_Input = int(input("What is your starting X coordinate: "))
    disy1_Input = int(input("What is your starting Y coordinate: "))
    disx2_Input = int(input("What is your ending X coordinate: "))
    disy2_Input = int(input("What is your ending Y coordinate: "))
    #get results
    disxs = disx2_Input-disx1_Input
    disxsfin = disxs**2
    disys = disy2_Input-disy1_Input
    disysfin = disys**2
    disformfinal = math.sqrt(disxsfin+disysfin)
    disformfinal = round(disformfinal, 2)
    print(f"Your distance is {disformfinal}")
    exit()
  else:
    pass

  if user_Input.upper() == "B":
    #show formula
    print("The formula for meters to feet is 1 meter per 3.28084 feet.")
    #ask for inputs
    mtr_Input = int(input("How many meters: "))
    #get results
    mtrfinal = mtr_Input*3.28084 
    mtrfinal = round(mtrfinal, 2)
    print(f"You will have {mtrfinal} feet.")
    exit()
  else:
    pass

  if user_Input.upper() == "C":
    #show formula
    print("The formula for for kilometers to miles is 1 kilometer per 0.621371 miles.")
    #ask for inputs
    mil_Input = int(input("How many kilometers: "))
    #get results
    milfinal = mil_Input*0.621371
    milfinal = round(milfinal, 2)
    print(f"You will have {milfinal} miles.")
    exit()
  else:
    pass
else:
  pass
print("This is not a valid input")