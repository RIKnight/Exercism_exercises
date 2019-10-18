#! /usr/bin/env python
"""
    Name:
        raindrops.py
    Purpose:
        exercism, python track, raindrops
    Written by:
        Z Knight, 2019.10.13
    Modified to use list appending; ZK, 2019.10.17
"""
def convert(number):
    result = []
    if number % 3 == 0:
        result.append("Pling")
    if number % 5 == 0:
        result.append("Plang")
    if number % 7 == 0:
        result.append("Plong")
    if result == []:
        return str(number)
    return "".join(result)

