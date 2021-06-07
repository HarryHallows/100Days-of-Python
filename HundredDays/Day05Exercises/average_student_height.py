studentHeights = input("Input a list of student heights \n").split(", ")

for i in range(0, len(studentHeights)):
    studentHeights[i] = int(studentHeights[i])
   

totalHeight = 0

for height in studentHeights:
    totalHeight += height


numberOfStudents = 0

for student in studentHeights:
    numberOfStudents += 1

averageHeight = totalHeight /numberOfStudents

print(f"The average student height is {averageHeight}cm") 

