#!/usr/bin/python3
"""
    This module can compare two classes
"""


def is_same_class(obj, a_class):
    """
        Compare two objects, checking if
        one is an instance of the other

        Args:
            obj (obj): object to be checked
            a_class (obj): class to be compared to
    """
    return type(obj) == a_class
