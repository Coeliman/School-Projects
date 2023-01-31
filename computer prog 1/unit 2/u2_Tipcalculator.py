print("You have 20 dollars")
bill = float(input("What is your total bill? "))
tip = int(input("What is your tip% amount? "))
split = int(input("How many ways will the bill be split? "))

tip2 = tip/100
tip_Amt = bill * tip2
total = bill + tip_Amt
totalfin = round(total, 2)
tip_Amtfin = round(tip_Amt, 2)
billfin = round(bill, 2)
print(f"Your tip is ${tip_Amtfin}, your total bill is ${totalfin}")
totalfin
splitbil = totalfin / split
splitbilrnd = round(splitbil, 2)
print(f"Each person will pay ${splitbilrnd}")

cashshrt = splitbil-20
cashshrtrnd = round(cashshrt, 2)
if cashshrtrnd >= 0:
  print(f"You are too poor, you are ${cashshrtrnd} short.")
else:
 pass