def extract_words(s, k):
    words = []
    for word in s.split():
        if word[:k] == k:
            words.append(word)
    return words

print(extract_words("The quick brown fox jumps over the lazy dog", 3))

"""

# Solution:

def extract_words(s, k):
    words = []
    for word in s.split():
        if word[:k] == k:
            words.