def get_book_text(filepath):
    with open(filepath) as f:
        book_text = f.read().lower()
    return str(book_text)

def get_words(book_text):
    words = book_text.split()
    return words

def get_char_count(words):
    char_count = {}
    chars = []
    for word in words:
        for char in word:
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1
    return char_count

def sort_on(list_dict):
    return list_dict["num"]

def sort_char(char_count):
    list_dict = []
    for char in char_count:
        dic = {"char": char, "num": char_count[char]}
        list_dict.append(dic)
    list_dict.sort(reverse=True, key=sort_on)
    return list_dict


