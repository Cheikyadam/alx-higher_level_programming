#!/usr/bin/python3
"""Class Rectangle"""
from models.base import Base


class Rectangle(Base):
    """ Class rectangle

    Attributes:
        x (int)
        y (int)
        width (int)
        height (int)
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """The constructor with all attributes"""
        super().__init__(id)
        self.__x = x
        self.__y = y
        self.__width = width
        self.__height = height

    @property
    def x(self):
        """to retrieve x"""
        return self.__x

    @x.setter
    def x(self, value):
        """to update x value"""
        self.__x = value

    @property
    def y(self):
        """To retrieve y value"""
        return self.__y

    @y.setter
    def y(self, value):
        """Updating y with value"""
        self.__y = value

    @property
    def width(self):
        """To retrieve width value"""
        return self.__width

    @width.setter
    def width(self, value):
        """"Update witdh value"""
        self.__witdh = value

    @property
    def height(self):
        """To retrieve height value"""
        return self.__height

    @height.setter
    def height(self, value):
        """"Update height value"""
        self.__height = value
