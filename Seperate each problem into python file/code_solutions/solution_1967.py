def even_length_words(s):
    for i in range(len(s)):
        if s[i] % 2 == 0:
            print(s[i])

s = input("Enter a string: ")
even_length_words(s)

"""

# Solution:

def even_length_words(s):
    for i in range(len(s)):
        if s[i] % 2 == 0:
            print(s[i])

s