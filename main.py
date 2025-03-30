from stats import get_num_words, get_char_count_dict, sorted_dictionary_list
import sys

if len(sys.argv) < 2:

    print(f"Usage: python3 main.py <path_to_book>")
    sys.exit(1)


book_path = sys.argv[1]

def main():

    num_words = get_num_words(book_path)
    character_count_dictionary = get_char_count_dict(book_path)
    new_dictionary_list = sorted_dictionary_list(character_count_dictionary)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")

    for i in new_dictionary_list:
        if i["char"].isalpha():
            print(i["char"] + ": " + str(i["count"]))

    print("============= END ===============")
   
main()

