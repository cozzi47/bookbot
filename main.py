def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    word_count = get_word_count(text)
    character_count = get_character_count(text)
    print(character_count)


def get_book_text(path):
    with open(path) as f:
        return f.read()


def get_word_count(text):
    words = text.split()
    return len(words)


def get_character_count(text):
    count = {}
    lowered = text.lower()
    for c in lowered:
        if c not in count:
            count[c] = 1
        else:
            count[c] += 1
    return count
    


main()


