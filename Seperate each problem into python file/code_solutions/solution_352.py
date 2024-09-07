def positive_numbers(iterable):
    for number in iterable:
        if number > 0:
            yield number

iterator = positive_numbers(range(10))

print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(