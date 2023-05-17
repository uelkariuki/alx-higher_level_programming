#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list is None:
        return 0
    score = [item[0] for item in my_list]
    weight = [item[1] for item in my_list]
    weighted_sum = sum(score * weight for score, weight in zip(score, weight))
    total_sum_weight = sum(weight)
    weight_average = weighted_sum / total_sum_weight
    return weight_average
