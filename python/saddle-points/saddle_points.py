
#! /usr/bin/env python
"""
    Name:
        saddle_points.py
    Purpose:
        exercism, python track, saddle pointss: 
            Detect saddle points in a matrix.
    Written by:
        Z Knight, 2020.09.18
"""
def saddle_points(matrix):
    """
    Input: matrix.
    Output: list of points; list of ordered (x,y) pairs, where each ordered pair is a length 2 list.
        In python: list[y][x]; use x for the first index; x is the column coordinate, y is the row
    """
    row_maxima_indices = []
    column_maxima_indices = []
    for row_index, row in enumerate(matrix):
        row_max = row[0]
        row_max_index = 0
        column_maximum_values = row[0]
        column_maximum_indices = {{{list of 0s}}}  # look this up
        
        for column_index, value in enumerate(row):
            if value > row_max:
                row_max = value
                row_max_index = column_index
            if value < column_maximum_values[column_index]:
                column_maximum_values[column_index] = value
                column_maximum_indices[column_index] = row_index
        row_maxima_indices.append(row_max_index)

    # stitch them together
    # do the column maxima line up with the row maxima?
    

    return row_maxima_indices, column_maxima_indices
