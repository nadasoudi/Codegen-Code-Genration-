def longest_word(s):
    words = s.split()
    longest = ""
    for word in words:
        if len(word) > len(longest):
            longest = word
    return longest

print(longest_word("The quick brown fox jumps over the lazy dog."))

"""

def longest_word(s):
    words = s.split()
    longest = ""
    for word in words:
        if len(word) > len(longest):