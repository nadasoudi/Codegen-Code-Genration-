def sort_dict(d):
    return sorted(d.items(), key=lambda item: item[1])

d = {
    "a": 1,
    "b": 2,
    "c": 3,
    "d": 4,
    "e": 5,
    "f": 6
}

print(sort_dict(d))

"""

def sort_dict(d):
    return sorted(d.items(), key=lambda item: item[1])