#! /usr/bin/env python
"""
    Name:
        armstrong_numbers.py
    Purpose:
        exercism, python track, armstrong numbers: determine whether a number is an Armstrong number.
    Written by:
        Z Knight, 2019.10.24
"""

def is_armstrong_number(number):
    reduced_number = number
    num_digits = 0
    partial_sum = 0

    # count the digits
    while reduced_number >= 1:
        reduced_number /= 10
        num_digits += 1

    # separate input into digits and raise to power
    reduced_number = number
    while reduced_number >= 1:
        my_digit = reduced_number % 10
        print(my_digit)
        reduced_number = int(reduced_number / 10)
        partial_sum += my_digit**num_digits
    if partial_sum == number:
        return True

    return False

    
