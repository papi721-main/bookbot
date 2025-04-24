#!/usr/bin/env python3
"""
main.py

The entry point to our program and any code that doesn't fit elsewhere
"""


def get_book_text(file_path: str):
    """
    Takes a file path as a string and returns
    the contents of the file as a string

    Args:
        file_path (str): path to the file

    Returns:
        str: contents of the file
    """
    with open(file_path) as f:
        file_contents = f.read()

    return file_contents


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


def main():
    """Main Function"""

    file_contents = get_book_text("./books/frankenstein.txt")
    num_words_message = get_number_of_words(file_contents)
    print(num_words_message)


if __name__ == "__main__":
    main()
