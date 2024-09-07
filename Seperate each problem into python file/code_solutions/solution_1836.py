import re

def is_start_with_substring(str, sub):
    return re.search(sub, str)

print(is_start_with_substring("Python is a programming language", "P"))
print(is_start_with_substring("Python is a programming language", "P"))
print(is_start_with_substring("Python is a programming language", "P"))
print(is_start_with_substring("Python is a programming language", "P