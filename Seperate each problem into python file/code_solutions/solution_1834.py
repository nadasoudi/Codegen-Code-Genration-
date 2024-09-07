def mirror_characters(string):
    mirror_dict = {}
    for char in string:
        if char in mirror_dict:
            mirror_dict[char] += 1
        else:
            mirror_dict[char] = 1
    return mirror_dict

print(mirror_characters("abcdefghijklmnopqrstuvwxyz"))

"""

def mirror_characters(string):
    mirror_dict = {}
    for char in string: