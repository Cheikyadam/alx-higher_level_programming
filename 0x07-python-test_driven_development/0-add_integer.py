#!/usr/bin/python3
def add_integer(a, b=98):
    """
    To add two integers

    Parameters:
        a (int): the firs parameter
        b (int): the second one

    Returns:
        int: the sum of a and b
    """
    if type(a) is not int:
        if type(a) is not float:
            raise TypeError("a must be an integer")
    if type(b) is not int:
        if type(b) is not float:
            raise TypeError("b must be an integer")
    a = int(a)
    b = int(b)
    return a+b
