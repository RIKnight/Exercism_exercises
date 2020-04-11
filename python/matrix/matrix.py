#! /usr/bin/env python
"""
    Name:
        matrix.py
    Purpose:
        exercism, python track, matrix: 
            Given a string representing a matrix of numbers, return the rows and columns of that matrix.
    Written by:
        Z Knight, 2020.04.08
    Modified to have single line functions; ZK, 2020.04.10
"""
class Matrix:
    def __init__(self, matrix_string):
        self.matrix = [[int(char) for char in row.split()] for row in matrix_string.split("\n")] 

    def row(self, index):
        return self.matrix[index-1]

    def column(self, index):
        return [row[index-1] for row in self.matrix]
