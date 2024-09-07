def product(numbers):
    return reduce(lambda x, y: x * y, numbers)

print(product([1, 2, 3, 4, 5]))

"""

# Solution 1

def product(numbers):
    return reduce(lambda x, y: x * y, numbers)

print(product([1, 2, 3, 4, 5]))

# Solution 2

def product(numbers):
    return reduce(lambda x, y