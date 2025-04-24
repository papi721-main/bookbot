#!/usr/bin/env python3
"""
stats.py

This file contains functions for analyzing texts
"""


def get_number_of_words(text: str):
    """
    Takes the text of a file as a string and returns the number of words
    in the text, using a string format

    Args:
        text (str): the text in the file

    Returns:
        str: number of words in the text, using a string format
    """
    num_words = len(text.split())
    return f"{num_words} words found in the document"


def get_character_counts(text: str):
    """
    Takes the text of a file as a string and returns the number of times
    each character (including symbols and spaces), appear in the text

    Args:
        text (str): the text in the file

    Returns:
        dict: a dictionary containing the count of each character in the text
    """
    character_count = {}
    for ch in text:
        ch = ch.lower()
        if ch in character_count:
            character_count[ch] += 1
        else:
            character_count[ch] = 1
    return character_count
