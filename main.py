from stats import word_count
from stats import count_characters
from stats import sort_dict
def main():
    path_as_string = "books/frankenstein.txt"
    path = get_book_text(path_as_string)
    num_words = word_count(path)
    num_chars = count_characters(path)
    sort_list = sort_dict(num_chars)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path_as_string}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    #print(num_chars)
    #print(sort_list)
    for chars in sort_list:
        print(f"{chars['char']}: {chars['num']}")
    
    print("============= END ===============")

def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
    return file_contents

main()