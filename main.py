#!/usr/bin/env python3
"""main.py"""


def get_book_text(filepath: str):
    """
    Takes a file path as a string and returns
    the contents of the file as a string

    Args:
        filepath (str): file path

    Returns:
        str: contents of the file
    """
    with open(filepath) as f:
        file_contents = f.read()

    return file_contents


def main():
    """Main Function"""

    contents = get_book_text("./books/frankenstein.txt")
    print(contents)


if __name__ == "__main__":
    main()
