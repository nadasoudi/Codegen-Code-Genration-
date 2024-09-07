import re

def split_string(string, delimiter):
    return re.split(delimiter, string)

print(split_string("This is a string", " "))

"""

# Solution 1

def split_string(string, delimiter):
    return string.split(delimiter)

print(split_string("This is a string", " "))

# Solution 2

def split_string(string, delimiter):
    return