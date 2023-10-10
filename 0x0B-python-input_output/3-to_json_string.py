#!/usr/bin/python3
"""
    This module handles JSON representation
"""
import json


def to_json_string(my_obj):
    """
        return the JSON representation of an object

        Args:
            my_obj (obj): object to be converted
    """
    return json.dumps(my_obj)
