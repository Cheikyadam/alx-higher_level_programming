#!/usr/bin/python3
"""Class Square """
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ A simple class square"""

    def __init__(self, size):
        """ To init the square

        Parameters:
            size (int): the size of the square
        """
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """Implementing area method

            Returns:
                area of the square
        """
        return self.__size * self.__size

    def __str__(self):
        """str methods"""
        return f"[Rectangle] {self.__size}/{self.__size}"
