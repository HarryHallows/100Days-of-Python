import random

bankerNames = input("Gove me everybody who's playing's name separated by a comma.\n")

names = bankerNames.split(", ")

nameNumb = len(names)

randomChoice = random.randint(0, nameNumb - 1)

personToPay = names[randomChoice]

print(personToPay + "will buy the meal today")