"""

word = input("Enter a word: ")
word = word.lower()
word = word.split()
word = word[::-1]
print(" ".join(word))