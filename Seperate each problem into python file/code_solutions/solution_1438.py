import re

def remove_words(words, char):
    for word in words:
        if re.search(char, word):
            words.remove(word)
    return words

print(remove_words(['hello', 'world', 'python', 'programming', 'is', 'fun', '?'], '?'))

"""

def remove_words(words, char):
    for word in words:
        if re.search(char, word):