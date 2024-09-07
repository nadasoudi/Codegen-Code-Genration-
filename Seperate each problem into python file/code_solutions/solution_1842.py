def find_duplicate(string):
    duplicate = []
    for i in string:
        if i in duplicate:
            duplicate.remove(i)
        else:
            duplicate.append(i)
    return duplicate

print(find_duplicate("abcdefg"))

"""

def find_duplicate(string):
    duplicate = []
    for i in string:
        if i in duplicate:
            duplicate.remove(i)