def update_tuple(tuple):
    for i in range(len(tuple)):
        tuple[i] = tuple[i] + 1
    return tuple

tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(update_tuple(tuple))

"""

# Solution:

def update_tuple(tuple):
    for i in range(len(tuple)):
        tuple[i] =