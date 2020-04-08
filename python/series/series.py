#! /usr/bin/env python
"""
    Name:
        series.py
    Purpose:
        exercism, python track, series: 
            Given a string of digits, output all the contiguous substrings of length n in that string in the order that they appear.
    Written by:
        Z Knight, 2020.04.07
"""
def slices(series, length):
    slice_list = []
    n_digits = len(series)
    if n_digits == 0:
        raise ValueError("Don\'t use an empty string!")
    if length <= 0 or length > n_digits:
        raise ValueError("That length is not possible.  Stop bragging.")
    for slice_num in range(n_digits-length+1):
        slice_list.append(series[slice_num:slice_num+length])

    return slice_list
