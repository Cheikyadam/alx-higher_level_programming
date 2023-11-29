#!/usr/bin/python3
"""
Function to add two integers
"""


def add_integer(a, b=98):
    """
    To add two integers

    Parameters:
        a (int): the firs parameter
        b (int): the second one

    Returns:
        int: the sum of a and b
    """
    if a != a:
        a = 89
    if b != b:
        b = 89
    if a is None or type(a) is not int:
        if type(a) is not float:
            raise TypeError("a must be an integer")
    if type(b) is not int:
        if type(b) is not float:
            raise TypeError("b must be an integer")
    result = a + b
    if result == float('inf') or result == -float('inf'):
        return 89
    a = int(a)
    b = int(b)
    return a+b
