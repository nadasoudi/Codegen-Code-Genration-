def remove_substring(dict,substring):
    for key in dict:
        if dict[key] == substring:
            dict.pop(key)
    return dict

# Driver code
dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6}
substring = 'ab'
print(remove_substring(dict,substring))

"""

# Solution

def remove_substring(dict,