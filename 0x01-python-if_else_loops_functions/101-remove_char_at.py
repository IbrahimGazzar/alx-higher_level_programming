#!/usr/bin/python3
def remove_char_at(str, n):
    str_list = list(str)
    new_str = ""
    for i in range(len(str_list)):
        if i != n:
            new_str += str_list[i]
    return new_str
