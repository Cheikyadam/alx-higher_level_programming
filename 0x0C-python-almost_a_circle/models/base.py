#!/usr/bin/python3
"""Base classe"""


class Base:
    """A base classe for the project

    Attributes:
        __nb_objects (int): to count object
        id (int): the id
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """ To init an object

        Parameters:
            id (int): to identify the object
        """
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id
