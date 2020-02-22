import numpy as np


# I initially started with area formulas for each case, but found out about Heron's Formula for area regardless of type
def heronFormula(sides):
    s = sum(sides) / 2
    area = np.sqrt(s * (s - sides[0]) * (s - sides[1]) * (s - sides[2]))
    return area


numbers = []
count = 0
area = 0
while True:
    if count >= 3:
        break
    number = input("Enter a number: ")
    try:
        number = int(number)
    except:
        print("That was not a number")
        continue
    # We have a proper number
    numbers.append(number)
    count += 1
numbers.sort()
# check if not triangle
if numbers[0] + numbers[1] < numbers[2]:
    print("it's not a triangle")
    exit()

# check if equilateral
if numbers[0] == numbers[1] and numbers[1] == numbers[2]:
    print(" it is an equilateral triangle")

# check if isosels
if numbers[0] == numbers[1] or numbers[1] == numbers[2]:
    print("isosceles")

# check if right angle
if numbers[2] ** 2 == numbers[0] ** 2 + numbers[1] ** 2:
    print("right angle")
    area = numbers[0] * numbers[1]

# check if obtuse
if numbers[2] ** 2 > numbers[0] ** 2 + numbers[1] ** 2:
    print("obtuse angle")

if numbers[2] ** 2 < numbers[0] ** 2 + numbers[1] ** 2:
    print("acute angle")

area = heronFormula(numbers)
print("The Area is {} !".format(round(area, 2)))
