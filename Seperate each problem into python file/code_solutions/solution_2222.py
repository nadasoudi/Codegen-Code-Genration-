def is_heterogram(string):
    if len(string) == 1:
        return True
    else:
        return False

print(is_heterogram("abc"))
print(is_heterogram("abcd"))
print(is_heterogram("abcdef"))
print(is_heterogram("abcdefghijklmnopqrstuvwxyz"))

"""

def is_heterogram(string):
    if len(string)