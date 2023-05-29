#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    result = []
    for q in range(list_length):
        try:
            if isinstance(my_list_1[q], (int, float)) and \
                    isinstance(my_list_2[q], (int, float)):
                if my_list_2[q] != 0:
                    div_result = my_list_1[q] / my_list_2[q]
                else:
                    div_result = 0
                    print("division by 0")
            else:
                div_result = 0
                print("wrong type")
        except IndexError:
            div_result = 0
            print("out of range")
        finally:
            result.append(div_result)
    return result
