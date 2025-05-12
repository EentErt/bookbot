def count_words(text):
    # count the number of words in the string 
    word_list = text.split()
    # the count is the length of the list given by the split function
    count = len(word_list)
    return count