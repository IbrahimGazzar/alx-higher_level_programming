#!/usr/bin/python3
def weight_average(my_list=[]):
    avg = 0.0
    div = 0
    for i in my_list:
        avg += i[0] * i[1]
        div += i[1]
    if div > 0:
        return avg / div
    else:
        return 0
