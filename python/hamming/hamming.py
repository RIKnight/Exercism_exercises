#! /usr/bin/env python
"""
    Name:
        hamming.py
    Purpose:
        exercism, python track, hamming: 
            Calculate the Hamming Distance between two DNA strands.
    Written by:
        Z Knight, 2020.09.11
    Modified to use zip instead of enumerate; ZK, 2021.10.15
"""
def distance(strand_a, strand_b):
    """
    Inputs:
        strand_a, strand_b: two strings of characters to find hamming distance of
    Returns:
        The hamming distance between strand_a and strand_b
    """

    # check lengths
    if len(strand_a) != len(strand_b):
        raise ValueError("lengths unequal")

    # check each character
    distance = 0
    #for strand_index, protein in enumerate(strand_a):
    #    if protein != strand_b[strand_index]:
    #        distance +=1
    pairs = zip(strand_a, strand_b)
    for pair in pairs:
        if pair[0] != pair[1]:
            distance +=1
    return distance

