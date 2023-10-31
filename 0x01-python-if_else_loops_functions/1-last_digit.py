#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if isinstance(number, int):
    last = str(number)
    digit = int(last[-1:])
    if number < 0:
        digit = -digit
    if digit > 5:
        print("Last digit of", number, "is", digit, "and is greater than 5")
    elif digit == 0:
        print("Last digit of", number, "is", digit, "and is 0")
    else:
        print("Last digit of", number, "is", digit, end='')
        print(" and is less than 6 and not 0")
else:
    x = "5"
    y = 2
    z = x / y
