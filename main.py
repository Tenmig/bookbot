from stats import get_book_text
from stats import count_words

def main():
    words_count = count_words(get_book_text("books/frankenstein.txt"))
    print(f"Found {words_count} total words")

main()