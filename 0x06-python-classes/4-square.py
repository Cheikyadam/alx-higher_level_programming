#!/usr/bin/python3
"""
    Simple class to represent a square.

    Attributes:
        __size (int): the size of the square
"""


class Square:
    """Defining the class Square"""
    def __init__(self, size=0):
        """
        Initializes a new square.

        Parameters:
            size (int): the size of the square
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """
        Calculation of the area

        Returns:
            int: the area of the square
        """
        return self.__size * self.__size

    @property
    def size(self):
        """
        To get the size

        Returns:
            int: the size of the instance
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        To update the size

        Parameters:
            value (int): the new value of size
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
