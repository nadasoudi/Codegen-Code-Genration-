def remove_keywords(dict, keywords):
    for key in keywords:
        if key in dict:
            dict.pop(key)
    return dict

print(remove_keywords({"a": "apple", "b": "banana", "c": "car"}, ["apple", "banana"]))

"""

def remove_keywords(dict, keywords):
    for key in keywords:
        if key in dict:
            dict.pop(key)
    return dict

print(remove_