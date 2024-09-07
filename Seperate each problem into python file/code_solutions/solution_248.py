def smallest_word(string):
    word = string.split()
    smallest = word[0]
    largest = word[-1]
    return smallest, largest

print(smallest_word("The quick brown fox jumps over the lazy dog"))

"""

def smallest_word(string):
    word = string.split()
    smallest = word[0]
    largest = word[-1]
    return smallest, largest

print(smallest_word("The