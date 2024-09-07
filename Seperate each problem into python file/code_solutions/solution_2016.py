def count_vowels(string):
    vowels = set(['a', 'e', 'i', 'o', 'u'])
    count = 0
    for i in string:
        if i in vowels:
            count += 1
    return count

print(count_vowels("Python is a high-level general-purpose programming language")
print(count_vowels("The quick brown fox jumps over the lazy dog"))
print(count_vowels("The