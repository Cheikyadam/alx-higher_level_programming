#!/usr/bin/python3
def print_last_digit(number):
    last = str(number)
    digit = int(last[-1:])
    print("{:d}".format(digit), end='')
    return digit
