#!/usr/bin/python3
"""
Simple function to print a square with #
"""


def print_square(size):
    """
    Definition of the function

    Parameters:
        size (int): the sizr of the square
    """
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if size == 0:
        print("", end='')
    else:
        for i in range(0, size):
            for j in range(0, size):
                print("#", end="")
            print()
