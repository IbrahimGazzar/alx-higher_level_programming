#!/usr/bin/python3
"""
   This module contains the function to be tested for task 2
"""


def print_square(size):
    """
        This function prints a square, using hashes

        Args:
            @size: side length of the square to be printed
    """
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(0, size):
        for j in range(0, size):
            print("#", end="")
        print("")
