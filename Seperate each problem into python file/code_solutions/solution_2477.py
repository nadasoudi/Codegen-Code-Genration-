s = input("Enter a sentence: ")
countUpper = 0
countLower = 0
for i in s:
    if i.isupper():
        countUpper += 1
    elif i.islower():
        countLower += 1
print("Number of Upper case letters: ", countUpper)
print("Number of Lower case letters: ", countLower)

"""

# Solution:

s = input("Enter a sentence: ")
countUpper