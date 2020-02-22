string = input("Give me the text please")

if string[::3] == string[1::3] == string[2::3]:
    print("They are all tripled ")
else:
    print("They are not all tripled")
