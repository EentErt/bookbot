from stats import count_words
from stats import character_count
import sys

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        # convert the file contents to a string
        file_contents = f.read()
        return file_contents

def main():
    args = sys.argv
    if len(args) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    path_to_file = args[1]
    file_contents = get_book_text(path_to_file)
    word_count = count_words(file_contents)
    letter_count = character_count(file_contents)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path_to_file}")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for letter in letter_count:
        print(f"{letter["char"]}: {letter["num"]}")
    print("============= END ===============")
    pass

main()
    
