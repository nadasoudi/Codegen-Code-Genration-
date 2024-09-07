def remove_words(words, words_to_remove):
    for word in words:
        if word in words_to_remove:
            words.remove(word)
    return words

print(remove_words(['apple', 'banana', 'orange', 'grape', 'pear'], ['banana', 'apple']))

"""

def remove_words(words, words_to_remove):
    for word in words:
        if word in words_to_remove: