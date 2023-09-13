#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    kill_list = []
    for i, j in a_dictionary.items():
        if j == value:
            kill_list.append(i)
    for i in kill_list:
        del a_dictionary[i]
    return a_dictionary
