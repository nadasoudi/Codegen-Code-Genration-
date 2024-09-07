def negative_iterator(iterable):
    for element in iterable:
        if element < 0:
            yield element

iterator = negative_iterator([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator