def get_length(dictionary):
    total = 0
    for key in dictionary:
        total += len(dictionary[key])
    return total

print(get_length({'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6}))

"""

def get_length(dictionary):
    total = 0
    for key in dictionary:
        total += len(dictionary