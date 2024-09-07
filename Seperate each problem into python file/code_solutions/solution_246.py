d = {'a': 1, 'b': 2, 'c': 3}

l = []
for i in d:
    l.append((i, d[i]))

print(l)

# Output:
# [('a', 1), ('b', 2), ('c', 3)]

# Hint:
# Use the dictionary keys() method to get the keys in the dictionary.
# Use the values() method to get the values in the dictionary.
# Use