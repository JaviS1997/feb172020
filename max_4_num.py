numbers = []
count = 0
while True:
    if count >= 4:
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
print('The length of the list is {}'.format(len(numbers)))
print('The numbers are : {}'.format(numbers))
print("The maximum is {} ".format(numbers[3]))
