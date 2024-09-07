def cycle(iterable):
    for i in iterable:
        yield i

# Create a generator object
gen = cycle([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

# Print the first element of the generator object
print(next(gen))

# Print the second element of the generator object
print(next(gen))

# Print the third element of the generator object
print(next(gen))

# Print the fourth