#!/usr/bin/python3
"""
    This module contains a class that
    inherits the common object of type list
"""


class MyList(list):
    """
        A modified (better!) version of list
    """
    def print_sorted(self):
        """
            prints the list in a sorted fashion
        """
        list_sorted = self[:]
        list_sorted.sort()
        print(list_sorted)
        
