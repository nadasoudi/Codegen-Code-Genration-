import numpy as np

def generator(n):
    for i in range(n):
        yield i

arr = generator(15)

print(next(arr))
print(next(arr))
print(next(arr))
print(next(arr))
print(next(arr))
print(next(arr))
print(next(arr))
print(next(arr))
print(next(arr))
print(next(arr))
print(next(