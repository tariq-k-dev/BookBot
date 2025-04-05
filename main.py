import sys
import textwrap
from stats import get_num_words, letters_count


def get_book_text(book_path: str) -> str:
    """Get the text of a book from a file."""
    with open(book_path, "r") as f:
        book_text = f.read()
    return book_text


def main():
    """Main function to run the program."""
    if len(sys.argv) == 1:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    BOOK_PATH = sys.argv[1]
    book_text = get_book_text(BOOK_PATH)
    book_words = get_num_words(book_text)
    letter_count = letters_count(book_text)
    book_report = textwrap.dedent(f"""
    ============ BOOKBOT ============
    Analyzing book found at {BOOK_PATH}...
    ----------- Word Count ----------
    Found {book_words} total words
    --------- Character Count -------
    """)
    for letter, count in sorted(letter_count.items()):
        book_report += f"{letter}: {count}\n"
    book_report += "============= END ==============="
    print(book_report)


if __name__ == "__main__":
    main()
