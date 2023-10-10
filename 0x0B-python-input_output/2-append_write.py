#!/usr/bin/python3
"""
    This module handles file appending
"""


def append_write(filename="", text=""):
    """
        appends into a file

        Args:
            filename (str): name of the file
            text (str): text to be written
    """
    with open(filename, 'a', encoding="utf-8") as f:
        return f.write(text)
