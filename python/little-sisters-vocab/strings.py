#! /usr/bin/env python
"""
    Name:
        strings.py
    Purpose:
        exercism, python track, strings: 
            1. Add a prefix to a word
            2. Add prefixes to word groups
            3. Remove a suffix from a word
            4. Extract and transform a word
    Written by:
        Z Knight, 2021.11.07
"""

def add_prefix_un(word):
    """

    :param word: str of a root word
    :return:  str of root word with un prefix

    This function takes `word` as a parameter and
    returns a new word with an 'un' prefix.
    """

    return 'un'+word


def make_word_groups(vocab_words):
    """

    :param vocab_words: list of vocabulary words with a prefix.
    :return: str of prefix followed by vocabulary words with
             prefix applied, separated by ' :: '.

    This function takes a `vocab_words` list and returns a string
    with the prefix  and the words with prefix applied, separated
     by ' :: '.
    """

    return_list = [vocab_words[0]]
    for word in vocab_words[1:]:
        return_list.append(vocab_words[0]+word)
    return " :: ".join(return_list)


def remove_suffix_ness(word):
    """

    :param word: str of word to remove suffix from.
    :return: str of word with suffix removed & spelling adjusted.

    This function takes in a word and returns the base word with `ness` removed.
    """

    base_word = word[:-4]
    if base_word[-1] == 'i':
        return base_word[:-1]+"y"
    else:
        return base_word


def noun_to_verb(sentence, index):
    """

    :param sentence: str that uses the word in sentence
    :param index:  index of the word to remove and transform
    :return:  str word that changes the extracted adjective to a verb.

    A function takes a `sentence` using the
    vocabulary word, and the `index` of the word once that sentence
    is split apart.  The function should return the extracted
    adjective as a verb.
    """

    base_word = sentence.split()[index]
    if base_word[-1] == ".":
        base_word = base_word[:-1]
    return base_word+"en"
