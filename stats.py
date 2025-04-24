#!/usr/bin/env python3
"""
stats.py

This file contains functions for analyzing texts
"""


def get_number_of_words(file_content: str):
    """
    Takes the content of a file as a string
    and returns the number of words in a string

    Args:
        file_content (str): the contents of a file

    Returns:
        str: number of words in the file, using a string format
    """
    num_words = len(file_content.split())
    return f"{num_words} words found in the document"


def get_character_counts(file_content: str):
    """
    Takes the content of a file as a string and returns the number of times
    each character (including symbols and spaces), appear in the file

    Args:
        file_content (str): the contents of a file

    Returns:
        dict: a dictionary containing the count for each character in the file
    """
    character_count = {}
    for ch in file_content:
        ch = ch.lower()
        if ch in character_count:
            character_count[ch] += 1
        else:
            character_count[ch] = 1
    return character_count
