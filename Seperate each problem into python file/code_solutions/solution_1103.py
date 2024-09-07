def compress(string):
    compressed = ""
    for i in string:
        if i not in compressed:
            compressed += i
    return compressed

print(compress("abcdefg"))

"""

def compress(string):
    compressed = ""
    for i in string:
        if i not in compressed:
            compressed += i
            compressed += str(len(compressed))
    return compressed