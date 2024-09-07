import re

def remove_words(text, words):
    for word in words:
        text = text.replace(word, "")
    return text

print(remove_words("Python is a programming language", ["Python", "programming"]))

"""

# Solution 1

def remove_words(text, words):
    for word in words:
        if word in text:
            text = text.replace(word, "")
    return text

print(remove_words("Python is a