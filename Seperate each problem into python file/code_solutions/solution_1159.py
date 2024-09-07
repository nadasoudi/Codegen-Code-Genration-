def even_numbers(d):
    new_dict = {}
    for key, value in d.items():
        if key % 2 == 0:
            new_dict[key] = value
    return new_dict

print(even_numbers({1: 2, 3: 4, 5: 6, 7: 8, 9: 10, 11: 12, 12: 13}))

"""

def even_numbers(d):
    new_dict = {}
    for key