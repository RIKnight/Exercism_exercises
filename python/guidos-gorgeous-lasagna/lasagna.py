#! /usr/bin/env python
"""
    Name:
        lasagna.py
    Purpose:
        exercism, python track, lasagna:
            Program to help you cook a gorgeous lasagna from your favorite cookbook.
    Written by:
        Z Knight, 2021.10.18
"""
EXPECTED_BAKE_TIME = 40 # minutes
PREPARATION_TIME = 2 # minutes per layer

def bake_time_remaining(elapsed_bake_time):
    """
    Calculate the bake time remaining.

    :param elapsed_bake_time: int baking time already elapsed.
    :return: int remaining bake time derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """
    return EXPECTED_BAKE_TIME - elapsed_bake_time

def preparation_time_in_minutes(number_of_layers):
    """
    Return preparation time based on number of layers in lasagna
    
    :param number_of_layers: int number of layers in the lasagna
    :return: int number of minutes to prepare the layers

    The preparation time is proportonal to the number of layers,
    and can be calculated by this function.
    """
    return PREPARATION_TIME * number_of_layers

def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """
    Return elapsed cooking time.

    :param number_of_layers: int number of layers in the lasagna
    :param elapsed_bake_time: baking time elapsed so far
    :return: remaining baking time

    This function takes two numbers representing the number of layers & the time already spent 
    baking and calculates the total elapsed minutes spent cooking the lasagna.
    """
    return preparation_time_in_minutes(number_of_layers) + elapsed_bake_time



