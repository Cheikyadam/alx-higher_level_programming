#!/usr/bin/python3
"""
class Rectangle inherited geometry
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """The simple rectangle"""
    def __init__(self, width, height):
        """ init method

        Parameters:
            width (int): the width
            height (int): the height
        """

        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
