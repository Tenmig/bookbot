def get_book_text(filepath):
    with open(filepath) as f:
        book_text = f.read()
    return str(book_text)

def count_words(book_text):
    words = book_text.split()
    words_count = len(words)
    return words_count