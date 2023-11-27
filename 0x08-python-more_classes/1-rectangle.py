#!/usr/bin/python3
"""Simple Class to define a rectangle"""


class Rectangle:
    """The class Rectangle"""

    def __init__(self, width=0, height=0):
        """
        Initialize a new rectangle.

        Parameters:
            width (int): the width of the rectangle
            height (int): the height
        """
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        self.__width = width
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__height = height

    @property
    def width(self):
        """
        To get the width

        Returns:
            int: the width of the instance
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        To update the width

        Parameters:
            value (int): the new value of size
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        To get the height

        Returns:
            int: the height of the instance
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        To update the height

        Parameters:
            value (int): the new value of size
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
