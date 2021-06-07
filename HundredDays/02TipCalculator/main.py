print("Welcome to the tip Calculator\n")

totalBill = input("What was the total bill?\n" + "£")

percentageTip = input("What percentage of the bill would like to leave?\n")
howManyPeople = input("How many people would you like to split it the bill between?\n")

tip = float(totalBill) * float(percentageTip) / 100  
totalSplitted = float(totalBill) / float(howManyPeople)

totalToPayEach = totalSplitted + (tip / float(howManyPeople))

print(f"The total bill split should be £{round(totalSplitted, 2)} " +  f"the tip should be £{round(tip, 2)}\n" + f"This will be £{round(totalToPayEach, 2)} each")
