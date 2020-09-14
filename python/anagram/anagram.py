#! /usr/bin/env python
"""
    Name:
        anagram.py
    Purpose:
        exercism, python track, difference of squares: 
            Given a word and a list of candidates, select the sublist of anagrams of the given word.
    Written by:
        Z Knight, 2020.09.13
"""
def is_anagram(word,candidate):
    """
    Inputs:
        word: the string to find anagrams for
        candidate: a string to compare against
    Returns:
        True if anagram, False if not
    """
    letters = [char for char in candidate.lower()]
    for letter in word.lower():
            if letter not in letters:
                return False
            else:
                letters.remove(letter)
    return len(letters) == 0


def find_anagrams(word, candidates):
    """
    Inputs:
        word: the string to find anagrams for
        candidates: a list of strings to compare against
    Returns:
        A list of matching strings
    """
    matching = []
    for candidate_word in candidates:
        if is_anagram(word, candidate_word) and word.lower() != candidate_word.lower():
            matching.append(candidate_word)
    return matching

