#!/usr/bin/env python3
"""
main.py

The entry point to our program and any code that doesn't fit elsewhere
"""
from stats import get_character_counts, get_number_of_words


def get_book_text(file_path: str):
    """
    Takes a file path as a string and returns
    the contents of the file as a string

    Args:
        file_path (str): path to the file

    Returns:
        str: text in the file as string
    """
    with open(file_path) as f:
        text = f.read()

    return text


def main():
    """Main Function"""

    text = get_book_text("./books/frankenstein.txt")
    num_words_message = get_number_of_words(text)
    print(num_words_message)

    character_count = get_character_counts(text)
    print(character_count)


if __name__ == "__main__":
    main()
