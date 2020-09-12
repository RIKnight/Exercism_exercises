#! /usr/bin/env python
"""
    Name:
        isbn_verifier.py
    Purpose:
        exercism, python track, isbn verifier: 
            Given a string, check if it is a valid ISBN-10.
    Written by:
        Z Knight, 2020.09.11
"""

def get_digits(isbn):
    """
    input:
        a string for an isbn-10
    returns:
        a list of integers, where "X" has been replaced by 10
    notes:
        invalid characters are ignored
        "X" can only be the last (checksum) digit
    """
    number_list = []
    for list_index, character in enumerate(isbn):
        if character == "X" and list_index == len(isbn)-1:
            number_list.append(10)
        elif character.isdigit():
            number_list.append(int(character))
    return number_list


def get_checksum(number_list):
    """
    inputs:
        number_list: a list of numbers of length 10
    returns:
        x1 * 10 + x2 * 9 + x3 * 8 + x4 * 7 + x5 * 6 + x6 * 5 + x7 * 4 + x8 * 3 + x9 * 2 + x10 * 1
    """
    sum = 0
    for list_index, number in enumerate(number_list):
        sum += number*(10-list_index)
    return sum


def is_valid(isbn):
    number_list = get_digits(isbn)
    if len(number_list) != 10:
        return False
    checksum = get_checksum(number_list)
    
    return checksum % 11 == 0

