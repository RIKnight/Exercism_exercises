#! /usr/bin/env python
"""
    Name:
        high_scores.py
    Purpose:
        exercism, python track, high_scores: Manage a game player's High Score list.
        these methods return the highest score from the list, the last added score and the three highest scores.
    Modification History:
        Written by Z Knight, 2019.09.25
        Modified to use sorted(); ZK, 2020.03.29
"""

def latest(scores):
    return(scores[-1])


def personal_best(scores):
    return(max(scores))


def personal_top_three(scores):
    my_scores = scores
    best_scores = []
    n_scores = min([3,len(scores)])
    sorted_scores = sorted(scores, reverse=True)
    best_scores = sorted_scores[:n_scores]
    return best_scores

