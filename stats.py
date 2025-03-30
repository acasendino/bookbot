def get_num_words(book_path):   
    with open(book_path) as f:
        file_contents = f.read()
    split_words = len(file_contents.split())
    return split_words

def get_char_count_dict(book_path):
    with open(book_path) as f:
        file_contents = f.read()

    characters = list(file_contents.lower())

    character_count_dictionary = {}
    for i in characters:
        if i in character_count_dictionary:
            character_count_dictionary[i] += 1
        else:
            character_count_dictionary[i] = 1
    return character_count_dictionary

def sorted_dictionary_list(character_count_dictionary):
    new_dictiontary_list = []
    for key,value in character_count_dictionary.items():
        char_dictionary = {}
        char_dictionary["char"] = key
        char_dictionary["count"] = value
        new_dictiontary_list.append(char_dictionary)

    def sort_on(dict):
        return dict["count"]
    
    new_dictiontary_list.sort(reverse=True, key=sort_on)
    
    return new_dictiontary_list
