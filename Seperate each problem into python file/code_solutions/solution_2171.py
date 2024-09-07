def convert_tuple(tup):
    d = {}
    for i in tup:
        for j in i:
            d[j] = i
    return d

tup = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(convert_tuple(tup))

"""

# Solution

def convert_tuple(tup):
    d = {}
    for i in tup:
        for j