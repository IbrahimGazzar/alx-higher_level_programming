#!/usr/bin/python3
"""
    This module handles simply file reading
"""


def read_file(filename=""):
    """
        This function simply reads a file

        Args:
            filename (str): name of the file
    """
    with open(filename, encoding="utf-8") as f:
        print(f.read())
