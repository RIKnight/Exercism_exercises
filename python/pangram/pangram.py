#! /usr/bin/env python
"""
    Name:
        pangram.py
    Purpose:
        exercism, python track, pangram
    Written by:
        Z Knight, 2019.09.15
"""

VALID_LETTERS = "abcdefghijklmnopqrstuvwxyz"
VALID_UPPERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def is_pangram(sentence):
    for index, letter in enumerate(VALID_LETTERS):
        if letter not in sentence and VALID_UPPERS[index] not in sentence:
            return False

    return True

