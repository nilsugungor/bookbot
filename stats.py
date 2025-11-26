def word_count(path):
    count = 0
    all_the_words = path.split()
    for word in all_the_words:
        count += 1
    return count

def count_characters(path):
    characters = path.lower()
    list_characters = list(characters)
    char_dict = {}
    for character in list_characters:
        if character in char_dict:
            char_dict[character] += 1
        else:
            char_dict[character] = 1
    return char_dict

def sort_on(items):
    return items["num"]

def sort_dict(char_dict):
    new_dict = {}
    for char in char_dict:
        if char.isalpha():
            new_dict[char] = char_dict[char]
    char_list = [{"char": k, "num": v} for k, v in new_dict.items()]
    char_list.sort(reverse=True, key=sort_on)
    return char_list