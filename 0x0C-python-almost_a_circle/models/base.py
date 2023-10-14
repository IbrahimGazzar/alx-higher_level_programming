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

    @classmethod
    def save_to_file(cls, list_objs):
        """
            takes a list of objects and saves
            their JSON representation to a file

            Args:
                list_objs (list): list of objects
                    to be saved
        """
        filename = str(cls.__name__) + ".json"
        list_json = []
        if list_objs is not None:
            for i in list_objs:
                list_json.append(dict(sorted(i.to_dictionary().items())))
        with open(filename, 'w', encoding="utf-8") as f:
            json.dump(list_json, f)

    @classmethod
    def create(cls, **dictionary):
        """
            Creates an object of type class with
            given attributes set

            Args:
                dictionary (dict): dict containing
                    the values to create with
        """
        if cls.__name__ == "Rectangle":
            obj = cls(1, 1)
        elif cls.__name__ == "Square":
            obj = cls(1)
        else:
            return None
        obj.update(**dictionary)
        return obj

    @staticmethod
    def to_json_string(list_dictionaries):
        """
            returns the JSON representation of a
            list of dictionaries

            Args:
                list_dictionaries (list): list of
                    dictionaries to be converted
        """
        if not list_dictionaries:
            return "[]"
        return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """
            Converts a json string of a list to a list

            Args:
                json_string (str): json string to be
                converted
        """
        if not json_string:
            return []
        return json.loads(json_string)
