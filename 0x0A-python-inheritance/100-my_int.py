#!/usr/bin/python3
"""Myint rebel"""


class MyInt(int):
    """ My rebel int"""

    def __eq__(self, other):
        """eq is not eq with my int"""
        if isinstance(other, MyInt) or isinstance(other, int):
            return not super().__eq__(other)
        return True

    def __ne__(self, other):
        """eq is not eq with my int"""
        if isinstance(other, MyInt) or isinstance(other, int):
            return not super().__ne__(other)
        return True
