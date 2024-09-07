def mergeDicts(dict1, dict2):
    dict1.update(dict2)
    return dict1

# Driver program to test above function
dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'d': 4, 'e': 5, 'f': 6}
print(mergeDicts(dict1, dict2))

"""

# Solution:

def mergeDicts(dict1, dict2):