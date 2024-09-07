def replace_words(dictionary, words):
    for word in words:
        dictionary[word] = dictionary.get(word, 0) + 1
    return dictionary

dictionary = {'apple': 2, 'banana': 1, 'orange': 1, 'grape': 1}
print(replace_words(dictionary, ['apple', 'banana', 'orange']))

"""

def replace_words(dictionary, words):
    for word in words:
        dictionary[word] = dictionary