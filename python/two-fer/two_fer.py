#! /usr/bin/env python
"""
    Name:
        two_fer.py
    Purpose:
        exercism, python track, two-fer exercise
    Modificaiton History:
        Written by Z Knight, 2019.09.08
"""

def two_fer(name=None):
    if name is None:
        name = 'you'
    return "One for {}, one for me.".format(name)
    
###############################################################################
# main

if __name__=="__main__":
    response = two_fer()
    print("response = {}".format(response))

    response = two_fer('Zaphod')
    print("response = {}".format(response))
