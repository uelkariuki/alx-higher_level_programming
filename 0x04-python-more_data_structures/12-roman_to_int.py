#!/usr/bin/python3
def roman_to_int(roman_string):
    if type(roman_string) is not str or roman_string is None:
        return 0
    roman_dict = {'I': 1, 'IV': 4, 'V': 5, 'IX': 9, 'X': 10, 'XL': 40,
                  'L': 50, 'XC': 90, 'C': 100,
                  'CD': 400, 'D': 500, 'CM': 900, 'M': 1000}
    total_num = 0
    q = 0

    while q < len(roman_string):
        if q + 1 < len(roman_string) and roman_string[q:q+2] in roman_dict:
            total_num = total_num + roman_dict[roman_string[q:q+2]]
            q = q + 2
        else:
            total_num = total_num + roman_dict[roman_string[q:q+1]]
            q = q + 1
    return total_num
