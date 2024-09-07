def count_vowels(string):
    vowels = set(['a', 'e', 'i', 'o', 'u'])
    count = 0
    for char in string:
        if char in vowels:
            count += 1
    return count

print(count_vowels("Python is a high-level general-purpose programming language"
                   " written in C++ and Fortran."))

"""

# Solution

def count_vowels(