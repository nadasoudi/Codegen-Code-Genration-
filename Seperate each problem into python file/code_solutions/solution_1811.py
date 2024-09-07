import itertools

def elementwise_and(a, b):
    return tuple(itertools.chain.from_iterable(itertools.combinations(a, 2)))

print(elementwise_and([1, 2, 3], [4, 5, 6]))

"""

# Solution

def elementwise_and(a, b):
    return tuple(itertools.chain.from_iterable(itertools.combinations(a, 2)))

print(element