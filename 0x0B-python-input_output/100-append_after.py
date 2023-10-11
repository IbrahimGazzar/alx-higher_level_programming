#!/usr/bin/python3
"""
    Appends text after text
"""


def append_after(filename="", search_string="", new_string=""):
    """
        Appends a given text after another given text in a file

        Args:
            filename (str): file to be modified
            search_string (str): string to be inserted after
            new_string (str): string to be inserted
    """
    with open(filename, 'r+', encoding='utf-8') as f:
        lines = f.readlines()
        f.seek(0)
        for line in lines:
            f.write(line)
            if search_string in line:
                f.write(new_string)
