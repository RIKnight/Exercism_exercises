#! /usr/bin/env python
"""
    Name:
        protein_translation.py
    Purpose:
        exercism, python track, protein_translation
    Written by:
        Z Knight, 2019.10.11
"""
def proteins(strand):
    # dictionary of protiens
    protein_dict = {
        "AUG": "Methionine",
        "UUU": "Phenylalanine",
        "UUC": "Phenylalanine",
        "UUA": "Leucine",
        "UUG": "Leucine",
        "UCU": "Serine",
        "UCC": "Serine",
        "UCA": "Serine",
        "UCG": "Serine",
        "UAU": "Tyrosine",
        "UAC": "Tyrosine",
        "UGU": "Cysteine",
        "UGC": "Cysteine",
        "UGG": "Tryptophan",
        "UAA": None,
        "UAG": None,
        "UGA": None }

    # break strand into segments
    num_segments = int(len(strand)/3)
    name_list = []
    for segment_num in range(num_segments):
        segment = strand[segment_num*3:segment_num*3+3]
        if segment in protein_dict:
            if protein_dict[segment] is None:
                return name_list
            else:
                name_list.append(protein_dict[segment])

    return name_list


