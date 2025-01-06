def main():
    
    path_to_book = "books/frankenstein.txt"
    book_content = get_book_contents(path_to_book)
    content_in_array = split_content(book_content)
    word_count = get_word_count(content_in_array)
    character_count = get_char_count(book_content)
    character_list = get_sorted_list_from_dict(character_count)

    print(f"--- Begin report of {path_to_book} ---")
    print(f"{word_count} words found in the document")
    print() #skip line

    print_character_count(character_list)
    print(f"--- End report ---")

def get_book_contents(path):

    with open(path) as f:
        file_contents = f.read()
        return file_contents

def split_content(content):

    words_array = content.split()
    return words_array

def get_word_count(words):
    
    word_count = len(words)
    return word_count

def get_char_count(text):
    char_dict = {}
    
    for char in text:
        lowered = char.lower()
        if lowered in char_dict:
            char_dict[lowered] += 1
        else:
           char_dict[lowered] = 1
    
    return char_dict

def print_character_count(char_list):

    for char in char_list:
        if char["char"].isalpha():
            print(f"The '{char}' character was found {char["char"]} times.")

def get_sorted_list_from_dict(char_dict):
    
    char_list = []
    for c in char_dict:
        char_list.append({"char": c, "num": char_dict[c]})

    char_list.sort(reverse=True, key=sort_on)
    return char_list

def sort_on(dict):
    return dict["num"]

main()