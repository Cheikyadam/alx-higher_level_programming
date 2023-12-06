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

    def to_json(self, attrs=None):
        """
        Function that returns the json represnetation \
                of a student
        """
        if attrs is None:
            return self.__dict__
        dico = dict()
        if "first_name" in attrs:
            dico['first_name'] = self.first_name
        if "last_name" in attrs:
            dico['last_name'] = self.last_name
        if "age" in attrs:
            dico['age'] = self.age
        return dico

    def reload_from_json(self, json):
        """
        To reload from a file"""
        self.first_name = json["first_name"]
        self.last_name = json["last_name"]
        self.age = json["age"]
