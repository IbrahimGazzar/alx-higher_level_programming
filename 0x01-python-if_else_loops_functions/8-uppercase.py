#!/usr/bin/python3
def uppercase(str):
    str_list = list(str)
    for i in range(len(str_list)):
        if ord(str_list[i]) in range(97, 123):
            str_list[i] = chr(ord(str_list[i]) - 32)
    new_str = ''.join(str_list)
    print("{}".format(new_str))
