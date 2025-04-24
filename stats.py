#!/usr/bin/env python3
"""
stats.py

This file contains functions for analyzing texts
"""


def get_words_count(text: str):
    """
    Takes the text of a file as a string and returns the number of words
    in the text, using a string format

    Args:
        text (str): the text in the file

    Returns:
        int: number of words in the text
    """
    words_count = len(text.split())
    return words_count


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


def sort_on_count(count_dict: dict):
    """Takes a dictionary returns the value of the 'count' key"""
    return count_dict["count"]


def get_sorted_character_counts(character_count: dict):
    """
    Takes the dictionary of characters and their counts and returns a sorted
    list of dictionaries

    Args:
        character_count (dict): dictionary containing the count of each
        character in the text

    Returns:
        list: a list of dictionaries containing the count of each
        character in the text, sorted by the character count
    """
    character_count_list = [
        {"char": ch, "count": character_count[ch]} for ch in character_count
    ]

    character_count_list.sort(key=sort_on_count, reverse=True)
    return character_count_list
