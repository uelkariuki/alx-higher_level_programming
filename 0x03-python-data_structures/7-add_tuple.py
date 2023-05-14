#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    tuple_a_result = tuple_a + (0, 0)
    tuple_b_result = tuple_b + (0, 0)
    return (tuple_a_result[0] + tuple_b_result[0], 
            tuple_a_result[1] + tuple_b_result[1])
