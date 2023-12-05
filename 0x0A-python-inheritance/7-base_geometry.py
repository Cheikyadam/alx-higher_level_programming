#!/usr/bin/python3
"""
Class Geometry
"""


class BaseGeometry:
    """Geometry class"""
    def area(self):
        """to find area"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ to check if value is an integer

        Parameters:
            name (str): the name of the value
            value (int): a value given
        """
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
