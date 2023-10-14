#!/usr/bin/python3
"""
    This module contains the base class that
    all others will inherit from
"""
import json


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """
            returns the JSON representation of a
            list of dictionaries

            Args:
                list_dictionaries: list of dictionaries
        """
        if not list_dictionaries:
            return "[]"
        return json.dumps(list_dictionaries)
