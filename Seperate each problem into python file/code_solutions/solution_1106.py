def reverse_string(string):
    if len(string) % 4 == 0:
        return string[::-1]
    else:
        return string

print(reverse_string("abcdefg"))

"""

def reverse_string(string):
    if len(string) % 4 == 0:
        return string[::-1]
    else:
        return string

print(reverse_string("abcdefg"))