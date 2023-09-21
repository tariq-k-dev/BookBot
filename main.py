from os import name, system

BOOK_PATH = "books/frankenstein.txt"


def clear() -> None:
    """Clears console at start of program."""
    if name == "nt":
        system("cls")
    else:
        system("clear")


def word_count(book) -> int:
    """Takes a book's text as input\nReturns total number of words."""
    return len(book.split())


def character_count(book: str) -> dict:
    """
    Takes a book's text as input.\n
    Returns a dictionary of letters as keys with their total counts as values.
    """

    letter_count = {}

    for char in book:
        if not char.isalpha():
            continue

        letter = char.lower()
        if letter not in letter_count:
            letter_count[letter] = 1
        else:
            letter_count[letter] += 1

    # Sort letter_count
    letter_keys = list(letter_count.keys())
    letter_keys.sort()
    sorted_letters = {key: letter_count[key] for key in letter_keys}

    return sorted_letters


def book_report(book_content: str) -> None:
    """Prints a summary of a books word and letter count inb the console"""

    clear()
    print(f"--- Begin report of {BOOK_PATH} ---\n")
    print(f"{word_count(book_content)} words found in the document\n")

    for letter, count in character_count(book_content).items():
        print(f"The '{letter}' character was found {count} times")
    print("\n--- End report ---\n")


# Get a book's text content, and generate a report
with open(BOOK_PATH) as f:
    file_contents = f.read()
    book_report(file_contents)
