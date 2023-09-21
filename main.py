# from string import ascii_lowercase
import json

BOOK_PATH = "books/frankenstein.txt"


def word_count(book):
    return len(book.split())


def character_count(book):
    letter_count = {}

    for char in book:
        # if char.lower() not in ascii_lowercase:
        #     continue

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


def book_report(book_content):
    print(f"--- Begin report of {BOOK_PATH} ---\n")
    print(f"{word_count(book_content)} words found in the document\n")

    # print(f"Frankenstein Book letter count: \n{json.dumps(character_count(book_content), indent=4)}")

    for letter, count in character_count(book_content).items():
        print(f"The '{letter}' character was found {count} times")
    print("\n--- End report ---\n")


with open(BOOK_PATH) as f:
    file_contents = f.read()

    book_report(file_contents)
