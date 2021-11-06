#! /usr/bin/env python
"""
    Name:
        grains.py
    Purpose:
        exercism, python track, grains: 
            Calculate the number of grains of wheat on a chessboard given that the number on each square doubles.
    Written by:
        Z Knight, 2021.11.06
"""

def square(number):
    if number < 1 or number > 64:
        print("error")
        raise ValueError("square must be between 1 and 64")
        return 0
    if number == 1:
        return 1
    return 2*(square(number-1))


def total():
    return square(64)*2-1
