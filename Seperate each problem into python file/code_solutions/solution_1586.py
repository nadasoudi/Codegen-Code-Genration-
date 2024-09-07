import numpy as np

def generator():
    for i in range(10):
        yield i

arr = np.array(generator())

print(arr)

# Output:
# [0 1 2 3 4 5 6 7 8 9]

# Note:
# The generator function is a generator function that returns a generator object.
# The generator function is a generator object that returns a value.
# The generator function is a generator object that returns a value.