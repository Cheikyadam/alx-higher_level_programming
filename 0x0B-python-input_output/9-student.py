#!/usr/bin/python3
"""
Class to represents a student
"""


class Student:
    """The class

    Attributes:
        first_name (str)
        last_name (str)
        age (int)
    """

    def __init__(self, first_name, last_name, age):
        """ To initiate a student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        Function that returns the json represnetation \
                of a student
        """
        return self.__dict__
