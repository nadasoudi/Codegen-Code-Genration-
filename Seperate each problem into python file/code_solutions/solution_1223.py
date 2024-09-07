def map_values(lst):
    d = {}
    for i in lst:
        d[i] = map(lambda x: x * x, lst)
    return d

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(map_values(lst))

"""