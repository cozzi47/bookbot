def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    word_count = get_word_count(text)
    character_count = get_character_count(text)
    letter_report = get_letter_report(book_path, word_count, character_count)
    

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
    

#def sort_on(character_count):
    return character_count["count"]
    
    
def get_letter_report(book_path, word_count, character_count):
    letters = []
    for character in character_count:
        count = character_count[character]
        if character.isalpha():
            letters.append((character, count))
    letters.sort(reverse=True, key=lambda x: x[1])   
    
    print (f"--- Begin report of {book_path} ---")  
    print (f"{word_count} words found in the document")
    print ()
    for character, count in letters:
        print(f"The '{character}' character was found {count} times")
    print(f"--- End report ---")
    
    


main()


