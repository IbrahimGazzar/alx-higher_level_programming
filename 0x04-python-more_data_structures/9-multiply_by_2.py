#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    dict_2 = {}
    for i, j in a_dictionary.items():
        dict_2[i] = j * 2
    return dict_2
