def longest_word(words):
    longest_word = ""
    longest_len = 0
    for word in words:
        if len(word) > longest_len:
            longest_word = word
            longest_len = len(word)
    return longest_word, longest_len

print(longest_word(["apple", "banana", "tacocat", "apple", "tacocat", "t