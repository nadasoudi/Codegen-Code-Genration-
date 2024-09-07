def palindrome(s):
    return s == s[::-1]

s = ["abcd", "cba", "dabcd", "cbad"]

print(list(filter(palindrome, s)))

"""

# Solution

def palindrome(s):
    return s == s[::-1]

s = ["abcd", "cba", "dabcd", "cbad"]

print(list(