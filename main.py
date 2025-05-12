from stats import count_words

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        # convert the file contents to a string
        file_contents = f.read()
        return file_contents

def main():
    file_contents = get_book_text("books/frankenstein.txt")
    word_count = count_words(file_contents)
    print(f"{word_count} words found in the document")
    pass

main()
    
