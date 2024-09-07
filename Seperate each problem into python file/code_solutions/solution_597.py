def symmetric_difference(a, b):
    return set(a) ^ set(b)

a = {1, 2, 3, 4, 5}
b = {4, 5, 6, 7, 8}

print(symmetric_difference(a, b))

# Output: {1, 2, 4, 5, 8}

# a = {1, 2, 3, 4, 5}
# b = {4,