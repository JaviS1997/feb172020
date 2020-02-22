def factorial(integer):
    if integer == 0:
        return 1
    else:
        result = integer
        return result * factorial(integer - 1)


print(factorial(4))
