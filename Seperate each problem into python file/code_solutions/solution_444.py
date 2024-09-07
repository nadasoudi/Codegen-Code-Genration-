def remove_words(words, words_to_remove):
    return [word for word in words if word not in words_to_remove]

print(remove_words(['apple', 'banana', 'carrot', 'apple', 'banana', 'carrot'], ['carrot', 'apple']))

"""

def remove_words(words, words_to_remove):
    return [word for word in words if word not in words_to_remove]

print(