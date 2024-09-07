def remove_duplicate_words(words):
    words_list = []
    for word in words:
        if word not in words_list:
            words_list.append(word)
    return words_list

print(remove_duplicate_words(["this", "is", "an", "example", "of", "this", "example"]))

"""

def remove_duplicate_