#!/usr/bin/python3
"""
Module that inherits list"""


class MyList(list):
    """
    Class that inherits list
    """
    def print_sorted(self):
        """
        To print sorted list
        """
        new = sorted(self)
        print(new)
