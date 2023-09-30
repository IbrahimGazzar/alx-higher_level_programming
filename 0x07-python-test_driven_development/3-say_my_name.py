#!/usr/bin/python3
"""
    This module contains the function needed for task 2
    of this python project
"""


def say_my_name(first_name, last_name=""):
    """
        This function prints the given inputs in the format:
            My name is <first name> <last name>

        Args:
            @first_name: string to be used as the first name
            @last_name: string to be used as the last name
                in case no second input is provided, it's replaced
                with an empty string
    """
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")

    print(f"My name is {first_name} {last_name}")
