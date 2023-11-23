#!/usr/bin/python3
"""
    Simple class to represent a square.

    Attributes:
        __size (int): the size of the square
"""


class Square:
    """Defining the class Square"""
    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes a new square.

        Parameters:
            size (int): the size of the square
            position (int, int): the position
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
        if (len(position) != 2) or (type(position[0]) != int):
            raise TypeError("position must be a tuple of 2 positive integers")
        if type(position[1]) is not int or position[0] < 0 or position[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = position

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

    @property
    def position(self):
        """
        To get the position

        Returns:
            (int, int):position the  of the instance
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        To update the position

        Parameters:
            value (int, int): the new value of size
        """
        if (len(position) != 2) or (type(position[0]) != int):
            raise TypeError("position must be a tuple of 2 positive integers")
        if type(position[1]) is not int or position[0] < 0 or position[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = position

    def my_print(self):
        """
        To print the square with #
        """
        if self.__size == 0:
            for t in range(0, self.__position[1]):
                print()
            for k in range(0, self.__position[0]):
                print(" ", end="")
            print()
        else:
            for t in range(0, self.__position[1]):
                print()
            for i in range(0, self.__size):
                for k in range(0, self.__position[0]):
                    print(" ", end="")
                for j in range(0, self.__size):
                    print("#", end="")
                print()
