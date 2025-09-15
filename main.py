from stats import get_num_words
from stats import get_char_count
from stats import sort_on
from stats import get_char_list
import sys

def main():
    if not len(sys.argv) == 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    char_count = get_char_count(text)
    count_list = get_char_list(char_count)
    count_list.sort(reverse=True, key=sort_on)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    
    for char in count_list:
        if char["char"].isalpha():
            print(f"{char["char"]}: {char["num"]}")
    

def get_book_text(book_filepath):
    with open(book_filepath) as f:
        return f.read()



main()