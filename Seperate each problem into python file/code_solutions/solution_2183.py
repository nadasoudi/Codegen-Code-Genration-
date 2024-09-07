def split_string(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    vowel_count = 0
    for char in string:
        if char in vowels:
            vowel_count += 1
    return vowel_count

print(split_string('Python is a high-level general-purpose programming language. Its design philosophy emphasizes code readability, and its syntax allows programmers to express concepts in fewer lines of code.'))

"""

def split_