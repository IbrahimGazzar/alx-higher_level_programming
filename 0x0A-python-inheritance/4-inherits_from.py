#!/usr/bin/python3
"""
    This module contains a function that determines
    if an object is a subclass of a given type/class
"""


def inherits_from(obj, a_class):
    """
        returns True if the object is an instance of
        a class that inherited (directly or indirectly)
        from the specified class ; otherwise False.
    """
    return (issubclass(type(obj), a_class) and type(obj) != a_class)
