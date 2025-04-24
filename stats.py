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
