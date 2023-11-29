#!/usr/bin/python3
"""
Simple function to print name
"""


def say_my_name(first_name, last_name=""):
    """
    Simple function to print names

    Parameters:
        first_name (str): the first parameter
        last_name (str): the second

    """
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    print(f"My name is {first_name} {last_name}")
