from decimal import Decimal

originalvalue = Decimal(input("How much money do you have?\n"))
dollarvalue = int(originalvalue) #This is the amount of single dollars they have
coinvalue = originalvalue - dollarvalue #This is the amount of coins that they have
Decimal(coinvalue)
#print(coinvalue, "1")

if coinvalue >= Decimal(0.25):
    quartervalue = Decimal(coinvalue) / Decimal(0.25) #It takes the number of quarters it has
    quartervalue = int(quartervalue)
    coinvalue -= quartervalue * Decimal(0.25)
    coinvalue = Decimal(coinvalue)
   # print(coinvalue, "2")
else:
    quartervalue = 0
if coinvalue >= Decimal(0.1):
    dimevalue = coinvalue / Decimal(0.1) #Number of nickels
    dimevalue = int(dimevalue)
    coinvalue -= dimevalue * Decimal(0.1)
    coinvalue = Decimal(coinvalue)
   # print(coinvalue, "3")
else:
    dimevalue = 0
  #  print(coinvalue, "303")
if coinvalue >= Decimal(0.05):
    nickelvalue = coinvalue / Decimal(0.05) #Number of Nickels
    #print(nickelvalue) #Should be 1.2
    nickelvalue = int(nickelvalue)
    #print(nickelvalue) #Should be 1
   # print(coinvalue, "new coinvalue")
    temp = nickelvalue * Decimal(0.05) #Temporary
    temp = round(temp, 2)
   # print(temp, "temp")
    coinvalue -= temp
    #coinvalue -= nickelvalue * Decimal(0.05)
    #print(coinvalue, "404")
    coinvalue = Decimal(coinvalue)
else:
    nickelvalue = 0

coinvalue = round(coinvalue, 2)
#print(coinvalue, "this game")

if float(coinvalue) >= Decimal(0.01):
    pennyvalue = coinvalue / Decimal(0.01) #Number of pennies
    pennyvalue = Decimal(pennyvalue)
    pennyvalue = round(pennyvalue, 2)
    pennyvalue = int(pennyvalue)
    #print(pennyvalue, "pennyvalue")
   # print(coinvalue, "penny coin value")
    templ = pennyvalue * Decimal(0.01)
   # print(templ, "templ")
    coinvalue -= templ
    coinvalue -= pennyvalue * Decimal(0.01)
    coinvalue = Decimal(coinvalue)
    #print(coinvalue, "5")
else:
    pennyvalue = 0
    #print("Hello")
print("You have", dollarvalue, "dollars,", quartervalue, "quarters,", dimevalue, "dimes,", nickelvalue, "nickels, and", pennyvalue, "pennies.")
