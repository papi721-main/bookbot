#!/usr/bin/env python3
"""
main.py

The entry point to our program and any code that doesn't fit elsewhere
"""
import sys

from stats import (
    get_character_counts,
    get_sorted_character_counts,
    get_words_count,
)


def get_book_text(file_path: str):
    """
    Takes a file path as a string and returns
    the contents of the file as a string
    """
    try:
        with open(file_path) as f:
            text = f.read()
        return text
    except Exception as e:
        print(e)
        sys.exit(1)


def print_report(
    file_path: str, words_count: int, character_count_sorted: list[dict]
):
    """Prints a report on the terminal"""
    print(
        f"""============ BOOKBOT ============
Analyzing book found at {file_path}
----------- Word Count ----------
Found {words_count} total words
--------- Character Count -------"""
    )
    for record in character_count_sorted:
        if record["char"].isalpha():
            print(f"{record['char']}: {record['count']}")
    print("============= END ===============")


def main():
    """Main Function"""

    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    file_path = sys.argv[1]

    text = get_book_text(file_path)
    words_count = get_words_count(text)

    character_counts = get_character_counts(text)
    character_counts_sorted = get_sorted_character_counts(character_counts)

    print_report(file_path, words_count, character_counts_sorted)


if __name__ == "__main__":
    main()
