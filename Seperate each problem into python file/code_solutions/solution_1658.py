def is_pangram(string):
    for i in range(len(string)):
        if string[i] not in alphabet:
            return False
    return True

print(is_pangram("The quick brown fox jumps over the lazy dog"))

"""

def is_pangram(string):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    for i in range(len(string)):
        if