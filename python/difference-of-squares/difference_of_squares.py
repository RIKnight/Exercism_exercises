#! /usr/bin/env python
"""
    Name:
        difference_of_squares.py
    Purpose:
        exercism, python track, difference of squares: 
            Find the difference between the square of the sum and the sum of the squares of the first N natural numbers.
    Written by:
        Z Knight, 2020.09.12
"""
def square_of_sum(number):
    """
    
    """
    sum = (number*(number+1))/2
    return sum**2


def sum_of_squares(number):
    """

    """
    sum = 0
    for num in range(1, number+1):
        sum += num**2
    return sum


def difference_of_squares(number):
    """
    Purpose: 
        Find the difference between the square of the sum and the sum of the squares of the first N natural numbers.
    Inputs:
        Number: the limit N
    Returns:
        The difference
    """
    return square_of_sum(number)-sum_of_squares(number)

