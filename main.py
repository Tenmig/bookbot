from stats import get_book_text
from stats import get_words
from stats import get_char_count
from stats import sort_char

import sys

def main():

    if len(sys.argv)<2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        file_path = sys.argv[1]
        words = get_words(get_book_text(file_path))
        words_count = get_char_count(words)
        sorted_char_list = sort_char(words_count)
        total_word = len(words)

        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {file_path}...")
        print("----------- Word Count ----------")
        print(f"Found {total_word} total words")

        print("--------- Character Count -------")
        # filtering out all the none alphabetic char from the list.
        alpha_char_list = [char for char in sorted_char_list if char["char"].isalpha()]
        for alpha in alpha_char_list:
            print(f"{alpha["char"]}: {alpha["num"]}

main()
