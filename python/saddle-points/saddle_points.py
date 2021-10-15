
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
        Refactored and completed; ZK, 2021.10.14
"""
def saddle_points(matrix):
    """
    Input: matrix.
    Output: list of points; list of ordered (x,y) pairs, where each ordered pair is a length 2 list.
        In python: list[y][x]; use x for the first index; x is the column coordinate, y is the row
    """
    # find matrix dimensions
    n_rows = len(matrix)
    n_cols = len(matrix[0])
    for row in matrix:
        if len(row) != n_cols:
            # throw an error
            pass

    # set up for finding max/min locations
    row_maxima_indices = []     # the column index of the max from each row
    column_minima_indices = []  # the row index of the min from each column
    
    # start with the first row for all column minima
    column_minima = matrix[0]
    for column in matrix[0]:
        column_minima_indices.append(0)
    
    for row_index, row in enumerate(matrix):
        # create a list to catch multiple row maxima
        print(f"row: {row}")
        row_maxima_list = []
        row_max = max(row)
        for col_index, col in enumerate(row):
            if col == row_max:
                row_maxima_list.append(col_index)
        row_maxima_indices.append(row_maxima_list)
        print(f"row maxima list: {row_maxima_list}")

        # continue search for column min, max:
        for column_index, value in enumerate(row):
            if value < column_minima[column_index]:
                column_minima[column_index] = value
                column_minima_indices[column_index] = row_index

    print(f"column min indices: {column_minima_indices}")
    print(f"row max indices: {row_maxima_indices}")
    # stitch them together
    # do the column maxima line up with the row minima?
    output_indices_list = []
    for column_index, column_min_row_index in enumerate(column_minima_indices):
        for row_max_index in row_maxima_indices[column_min_row_index]:
            if row_max_index == column_index:
                # add one to each to transform to 1-based counting format
                output_indices_list.append({"row":column_min_row_index+1, "column":column_index+1})

    return output_indices_list
