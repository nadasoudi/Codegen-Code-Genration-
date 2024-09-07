def clear_list(d):
    for i in d:
        d[i] = []

d = {'a': [1, 2, 3], 'b': [4, 5, 6], 'c': [7, 8, 9]}
clear_list(d)
print(d)

"""

# Solution:

def clear_list(d):
    for i in d:
        d[i] = []

d =