def multiply(numbers):
    return reduce(lambda x, y: x * y, numbers)

print(multiply([1, 2, 3, 4, 5]))

"""

# Solution 1

def multiply(numbers):
    return reduce(lambda x, y: x * y, numbers)

print(multiply([1, 2, 3, 4, 5]))

# Solution 2

def multiply(numbers):
    return reduce(lambda