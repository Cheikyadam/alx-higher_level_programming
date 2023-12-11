#!/usr/bin/python3
"""Now the square"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """The class square that inherits rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        """To init a square"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Printing a square"""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    @property
    def size(self):
        """To retrieve the size of a square"""
        return self.width

    @size.setter
    def size(self, value):
        """To update size"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """To update square attributes"""
        nb = len(args)
        if nb != 0:
            if nb >= 1:
                self.id = args[0]
            if nb >= 2:
                self.size = args[1]
            if nb >= 3:
                self.x = args[2]
            if nb >= 4:
                self.y = args[3]
        else:
            if kwargs is not None:
                for key, value in kwargs.items():
                    if key == "id":
                        self.id = value
                    elif key == "x":
                        self.x = value
                    elif key == "y":
                        self.y = value
                    elif key == "size":
                        self.size = value

    def to_dictionary(self):
        """To return dictionary repr of asquare"""
        return {'x': self.x, 'y': self.y, 'id': self.id, 'size': self.size}
