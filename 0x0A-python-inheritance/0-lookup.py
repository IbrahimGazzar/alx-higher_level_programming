#!/usr/bin/python3
"""
    This module contains a function
    that returns all attributes of an
    object
"""


def lookup(obj):
    """
        Lookup and return all attributes
        of an object

        Args:
            obj (object): object to be looked in
    """
    return dir(obj)
