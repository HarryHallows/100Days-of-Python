height = float(input("What is your height in metres:\n"))
weight = float(input("What is your weight in kg:\n"))

bmi = round(weight / height ** 2)

# round function rounds the float to the closest number up or down, this can also be rounded to the specified point by "print(round(bmi, 2)" 
# by combining the string statement with an f"example given {int variable example} " you then turn the string into an f-string this allows you to embed different variable types
# by encapsulating them between curly brackets
print(f"your bmi is {round(bmi)}")

if bmi < 18.5:
    print(f"Your bmi is {bmi}, you are underweight.")
elif bmi < 25:
    print(f"Your bmi is {bmi}, you have a normal weight")
elif bmi < 30:
    print(f"Your bmi is {bmi}, you are overweight")
elif bmi < 35:
    print(f"Your bmi is {bmi}, you are obese")
else:
    print(f"Your bmi is {bmi}, and you are clinically obese")

