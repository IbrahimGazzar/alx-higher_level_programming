#!/usr/bin/python3

""" This module contains a simple adding function
    to be appropriately tested using doctest """


def add_integer(a, b=98):
    """
        This function adds two values, and returns their summation

        Args:
            @a: first value to be added, must be int or float
            @b: second value to be added, must be int or float
                when no second input is provided, b is assumed to be equal 98
    """
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
