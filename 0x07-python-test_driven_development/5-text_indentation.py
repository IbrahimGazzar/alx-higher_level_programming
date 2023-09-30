#!/usr/bin/python3
"""
    This module contains the function to be tested for task 5
"""


def text_indentation(text):
    """
        This function takes a string and indents it in a
        specific format. Printing a new empty line after one
        of the following characters: '.', '?', ':'

        Args:
            @text: the string to be formatted
    """
    if type(text) is not str:
        raise TypeError("text must be a string")

    for i in range(0, len(text)):
        if i > 0 and text[i - 1] in ['.', '?', ':'] and text[i] == ' ':
            pass
        else:
            print(f"{text[i]}", end="")
        if text[i] in ['.', '?', ':']:
            print("\n")
