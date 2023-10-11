#!/usr/bin/python3
"""
    This module turns a class into jason
"""


def class_to_json(obj):
    """
        Convert a class obj into a json obj

        Args:
            obj (obj): class object to be converted
    """
    return obj.__dict__
