#! /usr/bin/env python
"""
    Name:
        perfect_numbers.py
    Purpose:
        exercism, python track, perfect_numbers: determine whether a number is "perfect"
    Written by:
        Z Knight, 2019.09.24
"""

def is_factor(to_check, maybe_factor):
    return to_check % maybe_factor == 0


def classify(to_check):
    if to_check == 1:
        return("deficient")
    if to_check <= 0:
        raise ValueError(r".+")
        return

    sum = 0
    for maybe_factor in range(1, to_check-1):
        if is_factor(to_check, maybe_factor):
            sum += maybe_factor

    if sum > to_check:
        return("abundant")
    if sum == to_check:
        return("perfect")
    return("deficient")

