#!/usr/bin/python3
"""
    This module contains a locked class
"""


class LockedClass():
    """
        This class prevents the addition of new
        attributes, except a secret first name one
    """
    __slots__ = ['first_name']
