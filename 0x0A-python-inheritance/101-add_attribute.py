#!/usr/bin/python3
"""To add attributes if possible"""


def add_attribute(obj, attr_name, attr_value):
    """The function below"""

    if hasattr(obj, '__dict__') or (hasattr(type(obj), '__slots__') and\
            attr_name in type(obj).__slots__):
        setattr(obj, attr_name, attr_value)
    else:
        raise TypeError("can't add new attribute")
