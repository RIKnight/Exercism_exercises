#! /usr/bin/env python
"""
    Name:
        hello_world.py
    Purpose:
        exercism, python track, exercise 1.
        Write a function (named 'hello') that returns the string "Hello, World!"
    Modificaiton History:
        Written by Z Knight, 2019.09.07
"""
def hello():
    return("Hello, World!")
    
###############################################################################
# main

if __name__=="__main__":
    response = hello()
    print("response = {}".format(response))

