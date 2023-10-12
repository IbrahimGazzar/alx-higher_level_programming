#!/usr/bin/python3
"""
    This module contains the base class that
    all others will inherit from
"""


class Base:
    """
        A basic class that handles ids

        Attributes:
            __nb_objects (int): number of objects
                created in this class
            id (int): individual object's id
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
            Intializing function for Base class

            Args:
                id (int): id of object
        """
        if id is not None:
            self.id = id
        else:
            type(self).__nb_objects += 1
            self.id = type(self).__nb_objects
