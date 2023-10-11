#!/usr/bin/python3
"""
    This module handles saving JSON representations
"""
import json


def save_to_json_file(my_obj, filename):
    """
        Saves a JSON representation of an object to a file

        Args:
            my_obj (obj): object to be converted
            filename (str): name of the file
    """
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(my_obj, f)
