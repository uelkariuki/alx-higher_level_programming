#!/usr/bin/python3

""" Function that finds a peak in a list of unsorted integers."""


def find_peak(list_of_integers):
    """ Function that finds a peak in a list of unsorted integers."""

    if not list_of_integers:
        return None
    nums = len(list_of_integers)
    left = 0
    right = nums - 1
    while (left < right):
        mid = left + (right - left) // 2
        if (list_of_integers[mid] < list_of_integers[mid + 1]):
            left = mid + 1
        else:
            right = mid
    return list_of_integers[left]
