def get_num_words(book: str) -> int:
    """Count the number of words in a book."""
    num_words = len(book.split())
    return num_words


def letters_count(book: str) -> dict:
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

    return letter_count


def sorted_letter_count(letters_dict: dict) -> list:
    """Return a sorted list of letters and their counts."""
    sorted_letters = sorted(letters_dict.items(),
                            key=lambda x: x[1], reverse=True)
    return sorted_letters
