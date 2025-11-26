from stats import word_count
from stats import count_characters

def main():
    path = get_book_text("books/frankenstein.txt")
    num_words = word_count(path)
    num_chars = count_characters(path)
    print(f"Found {num_words} total words")
    print(num_chars)

def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
    return file_contents

main()