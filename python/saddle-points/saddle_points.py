
#! /usr/bin/env python
"""
    Name:
        saddle_points.py
    Purpose:
        exercism, python track, saddle points: 
            Detect saddle points in a matrix.
    Written by:
        Z Knight, 2020.09.18 (started)
    Modified:
        Refactored and completed; ZK, 2021.10.15
"""
def saddle_points(matrix):
    """
    Input: matrix.
    Output: list of points; list of ordered (x,y) pairs, where each ordered pair is a dictionary:
        {"row":row,"column":column}, and the row and column numbers are indexed starting with 1
    """
    # catch empty matrix
    if matrix == []:
        return []

    # check for rectangular matrix
    n_cols = len(matrix[0])
    for row in matrix:
        if len(row) != n_cols:
            raise ValueError(".+")

    # set up for finding max/min locations
    row_maxima_indices = []     # the column index(es) of the max(s) from each row
    column_minima_indices = []  # the row index(es) of the min(s) from each column
    
    # start with the first row for all column minima
    column_minima = matrix[0]
    for column in matrix[0]:
        # create a list to catch multiple column minima
        column_minima_indices.append([0])
    
    for row_index, row in enumerate(matrix):
        # create a list to catch multiple row maxima
        row_maxima_list = []
        row_max = max(row)
        for col_index, col in enumerate(row):
            if col == row_max:
                row_maxima_list.append(col_index)
        row_maxima_indices.append(row_maxima_list)

        # continue search for column minima:
        for column_index, value in enumerate(row):
            if value < column_minima[column_index]:
                # new minimum found
                column_minima[column_index] = value
                column_minima_indices[column_index] = [row_index]
            elif value == column_minima[column_index] and row_index != 0:
                # multiple minima in column
                column_minima_indices[column_index].append(row_index)

    ## print(f"column min indices: {column_minima_indices}")
    ## print(f"row max indices: {row_maxima_indices}")
    
    # stitch them together
    # do the column maxima line up with the row minima?
    output_indices_list = []
    for column_index, column_min_row_index_list in enumerate(column_minima_indices):
        for column_min_row_index in column_min_row_index_list:
            for row_max_index in row_maxima_indices[column_min_row_index]:
                if row_max_index == column_index:
                    # add one to each to transform to 1-based counting format
                    output_indices_list.append({"row":column_min_row_index+1, "column":column_index+1})

    return output_indices_list
