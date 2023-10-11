#!/usr/bin/python3
"""
    Handles converting a JSON to object
"""
import json


def from_json_string(my_str):
    """
        Returns an object represented my a JSON string

        Args:
            my_str (str): JSON representation of an object
    """
    return json.loads(my_str)
