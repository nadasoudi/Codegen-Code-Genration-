def remove_lowercase_substrings(string):
    lowercase_substrings = []
    for i in string:
        if i.islower():
            lowercase_substrings.append(i)
    return lowercase_substrings

print(remove_lowercase_substrings("Python is a programming language"))

"""

def remove_lowercase_substrings(string):
    lowercase_substrings = []
    for i in string:
        if i.islower