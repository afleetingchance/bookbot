import sys
from stats import *

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    
    return file_contents

def print_report(filepath, word_count, char_counts):
    print('============ BOOKBOT ============')
    print(f"Analyzing book found at {filepath}")
    print('----------- Word Count ----------')
    print(f"Found {word_count} total words")
    print('--------- Character Count -------')
    for char_count in char_counts:
        print(f"{char_count['char']}: {char_count['num']}")
    print('============= END ===============')

def main():
    if len(sys.argv) != 2:
        print('Usage: python3 main.py <path_to_book>')
        sys.exit(1)

    filepath = sys.argv[1]
    text = get_book_text(filepath)
    num_words = get_word_count(text)
    char_count = get_character_count(text)
    print_report(filepath, num_words, char_count)

main()