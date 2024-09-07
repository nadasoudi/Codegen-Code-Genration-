s = "abcdefghijklmnopqrstuvwxyz"

def is_alphabet(s):
    for i in s:
        if i not in alphabet:
            return False
    return True

print(is_alphabet(s))

"""

alphabet = "abcdefghijklmnopqrstuvwxyz"

def is_alphabet(s):
    for i in s:
        if i not in alphabet: