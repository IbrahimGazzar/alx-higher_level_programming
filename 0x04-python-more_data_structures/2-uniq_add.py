#!/usr/bin/python3
def uniq_add(my_list=[]):
    sum = 0
    sub_list = [0]
    for i in my_list:
        if i not in sub_list:
            sub_list.append(i)
            sum += i
    return sum
