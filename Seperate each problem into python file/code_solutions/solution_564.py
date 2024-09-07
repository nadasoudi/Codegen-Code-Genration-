import collections

d = collections.OrderedDict()
d = collections.OrderedDict(sorted(d.items(), key=lambda item: item[0]))
print(d)

# Output:
# {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6}
# {'a': 1,