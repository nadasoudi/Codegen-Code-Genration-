def except_split(s):
    try:
        return s.split()
    except ValueError:
        return s

print(except_split("abcdefghi"))

"""

def except_split(s):
    try:
        return s.split()
    except ValueError:
        return s

print(except_split("abcdefghi"))

"""

def except_split(s):
    try:
        return s.split()
    except ValueError: