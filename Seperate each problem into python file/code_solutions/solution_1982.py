def add_tuple(tup1, tup2):
    return tuple(tup1[i] + tup2[i] for i in range(len(tup1)))

tup1 = (1, 2, 3, 4, 5)
tup2 = (6, 7, 8, 9, 10)

print(add_tuple(tup1, tup2))

"""

def add_tuple(tup1, tup2):