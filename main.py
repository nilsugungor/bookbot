import sys
from stats import word_count
from stats import count_characters
from stats import sort_dict
def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    path_as_string = sys.argv[1]
    path = get_book_text(path_as_string)
    num_words = word_count(path)
    num_chars = count_characters(path)
    sort_list = sort_dict(num_chars)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path_as_string}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for chars in sort_list:
        print(f"{chars['char']}: {chars['num']}")
    print("============= END ===============")
def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
    return file_contents

main()