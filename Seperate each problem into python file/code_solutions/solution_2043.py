def replace_multiple_words(s, words):
    for word in words:
        s = s.replace(word, "K" + word)
    return s

print(replace_multiple_words("Python is a programming language", ["Python", "programming"]))

"""

def replace_multiple_words(s, words):
    for word in words:
        s = s.replace(word, "K" + word)
    return s

print(replace_multiple_words("Python is a