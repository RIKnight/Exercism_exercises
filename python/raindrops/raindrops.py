#! /usr/bin/env python
"""
    Name:
        raindrops.py
    Purpose:
        exercism, python track, raindrops
    Written by:
        Z Knight, 2019.10.13
"""
def convert(number):
    result = ""
    if number % 3 == 0:
        result += "Pling"
    if number % 5 == 0:
        result += "Plang"
    if number % 7 == 0:
        result += "Plong"
    if result == "":
        return str(number)
    return result

