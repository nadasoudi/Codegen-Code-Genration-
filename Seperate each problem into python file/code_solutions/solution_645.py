def map_list(l1, l2):
    d = {}
    for i in l1:
        d[i] = l2.count(i)
    return d

l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
l2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(map_list(l1, l2))

"""

# Solution: