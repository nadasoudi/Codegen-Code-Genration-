import re

def strip_set(string):
    return re.sub('[^a-zA-Z0-9]', '', string)

print(strip_set('Python is a programming language'))

"""

# Solution:

def strip_set(string):
    return re.sub('[^a-zA-Z0-9]', '', string)

print(strip_set('Python is a programming language'))