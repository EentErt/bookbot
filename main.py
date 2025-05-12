from stats import count_words
from stats import character_count

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        # convert the file contents to a string
        file_contents = f.read()
        return file_contents

def main():
    file_contents = get_book_text("books/frankenstein.txt")
    word_count = count_words(file_contents)
    letter_count = character_count(file_contents)

    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"{word_count} words found in the document")
    print("--------- Character Count -------")
    for letter in letter_count:
        print(f"{letter["char"]}: {letter["num"]}")
    print("============= END ===============")
    pass

main()
    
