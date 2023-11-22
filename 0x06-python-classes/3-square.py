#!/usr/bin/python3
"""
    Simple class to represent a square.

    Attributes:
        __size (int): the size of the square
"""


class Square:
    def __init__(self, size=0):
        """
        Initializes a new square.

        Parameters:
            size (int): the size of the square
        """
        try:
            if type(size) is not int:
                raise TypeError("size must be an integer")
        except TypeError:
            print("size must be an integer")
        else:
            try:
                if size < 0:
                    raise ValueError("size must be >= 0")
            except ValueError:
                print("Size must be >= 0")
            else:
                self.__size = size

    def area(self):
        """
        Calculation of the area

        Returns:
            int: the area of the square
        """
        return self.__size * self.__size
