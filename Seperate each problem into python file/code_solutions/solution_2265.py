def swap_hierarchy(d):
    for i in d:
        for j in d[i]:
            d[i][j] = d[i][j][0]
    return d

d = {'a': {'b': {'c': 1, 'd': 2}, 'e': 3}, 'b': {'c': 4, 'd': 5}, 'c': 6, 'd': 7}
print(swap_hierarchy(d))

"""