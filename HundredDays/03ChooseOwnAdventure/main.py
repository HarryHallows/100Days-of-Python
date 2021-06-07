print("Welcome to the choose your own adventure!")

crossRoad = input("You find yourself at a crossroad, which direction would you like to take? 'left' or 'right'...\n").lower()




if crossRoad == "left":
    firstChoice = input("You stumble across a tavern, do you want to enter the tavern? 'yes' or 'no'..\n").lower()
    if firstChoice == "yes":
        tavernEnter = input("you enter the tavern and stumble across a bunch of old drunks inside, do you ask for 'information' or order 'food'?\n")
        if tavernEnter == "food":
            print("you suddenly feel unwell and a sharp pain crawling down your neck as you realise your food was poisoned..")
        else:
            print("You're given information about the surrounding area...")