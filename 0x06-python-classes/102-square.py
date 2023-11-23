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

    @property
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

    def __eq__(self, second_sq):
        """
        To compare 2 squares

        Parameters:
            second_sq (Square): the second

        Returns:
            boolean: True or False
        """
        if isinstance(second_sq, Square):
            return self.area == second_sq.area
        else:
            raise TypeError("Not instance of Square")

    def __ne__(self, second_sq):
        """
        To compare 2 squares

        Parameters:
            second_sq (Square): the second

        Returns:
            boolean: True or False
        """
        if isinstance(second_sq, Square):
            return self.area != second_sq.area
        else:
            raise TypeError("Not instance of Square")

    def __gt__(self, second_sq):
        """
        To compare 2 squares

        Parameters:
            second_sq (Square): the second

        Returns:
            boolean: True or False
        """
        if isinstance(second_sq, Square):
            return self.area > second_sq.area
        else:
            raise TypeError("Not instance of Square")

    def __ge__(self, second_sq):
        """
        To compare 2 squares

        Parameters:
            second_sq (Square): the second

        Returns:
            boolean: True or False
        """
        if isinstance(second_sq, Square):
            return self.area >= second_sq.area
        else:
            raise TypeError("Not instance of Square")

    def __lt__(self, second_sq):
        """
        To compare 2 squares

        Parameters:
            second_sq (Square): the second

        Returns:
            boolean: True or False
        """
        if isinstance(second_sq, Square):
            return self.area < second_sq.area
        else:
            raise TypeError("Not instance of Square")

    def __le__(self, second_sq):
        """
        To compare 2 squares

        Parameters:
            second_sq (Square): the second

        Returns:
            boolean: True or False
        """
        if isinstance(second_sq, Square):
            return self.area <= second_sq.area
        else:
            raise TypeError("Not instance of Square")
