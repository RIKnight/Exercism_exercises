#! /usr/bin/env python
"""
    Name:
        matrix.py
    Purpose:
        exercism, python track, matrix: 
            Given a string representing a matrix of numbers, return the rows and columns of that matrix.
    Written by:
        Z Knight, 2020.04.08
"""
class Matrix:
    def __init__(self, matrix_string):
        rows = matrix_string.split("\n")
        matrix = []
        for row in rows:
            row_chars = row.split()
            row_ints = []
            for char in row_chars:
                row_ints.append(int(char))
            matrix.append(row_ints)
        self.matrix = matrix

    def row(self, index):
        return self.matrix[index-1]

    def column(self, index):
        selected_column = []
        for row in self.matrix:
            selected_column.append(row[index-1])
        return selected_column
