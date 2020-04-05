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
        Modified to single-line personal_top_three function; ZK, 2020.04.04
"""

def latest(scores):
    return(scores[-1])


def personal_best(scores):
    return(max(scores))


def personal_top_three(scores):
    return sorted(scores, reverse=True)[:3]
