age = input("What is your current age?\n")
weeksEachYear = 52.143
ageToWeeks = float(age) * weeksEachYear

lifeSpan = 100 * weeksEachYear
timeLeftToLive =  lifeSpan - ageToWeeks

print(f"You have lived {round(ageToWeeks)} weeks so far!")

print(f"If you live until 100 years old, then you have {round(timeLeftToLive)} weeks left")