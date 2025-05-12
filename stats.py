def count_words(text):
    # count the number of words in the string 
    word_list = text.split()
    # the count is the length of the list given by the split function
    count = len(word_list)
    return count

def character_count(text):
    # initialize the letter dictionary
    letter_count = {}

    # count the letters
    for character in text:
        character = character.lower()
        if character not in letter_count:
            letter_count[character] = 0
        letter_count[character] += 1

    report = character_count_report(letter_count)
    return report

def character_count_report(character_dict):
    report = []

    for character in character_dict:
        if character.isalpha():
            dict = {}
            dict["char"] = character
            dict["num"] = character_dict[character]
            report.append(dict)

    report.sort(reverse = True, key = sort_on)
    return report

def sort_on(dict):
    return dict["num"]


    # go through the characters and add them to the dictionary