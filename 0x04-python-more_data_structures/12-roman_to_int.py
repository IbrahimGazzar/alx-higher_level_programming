#!/usr/bin/python3
def roman_to_int(roman_string):
    num = 0
    if not isinstance(roman_string, str):
        return 0
    leng = len(roman_string)
    for i in range(leng):
        if roman_string[i] == 'M':
            num += 1000
        elif roman_string[i] == 'D':
            num += 500
        elif roman_string[i] == 'C':
            if i + 1 < leng and roman_string[i + 1] == 'M':
                num += 900
                i += 1
            elif i + 1 < leng and roman_string[i + 1] == 'D':
                num += 400
                i += 1
            else:
                num += 100
        elif roman_string[i] == 'L':
            num += 50
        elif roman_string[i] == 'X':
            if i + 1 < leng and roman_string[i + 1] == 'C':
                num += 90
                i += 1
            elif i + 1 < leng and roman_string[i + 1] == 'L':
                num += 40
                i += 1
            else:
                num += 10
        elif roman_string[i] == 'V':
            num += 5
        elif roman_string[i] == 'I':
            if i + 1 < leng and roman_string[i + 1] == 'X':
                num += 9
                i += 1
            elif i + 1 < leng and roman_string[i + 1] == 'V':
                num += 4
                i += 1
            else:
                num += 1
    return num
