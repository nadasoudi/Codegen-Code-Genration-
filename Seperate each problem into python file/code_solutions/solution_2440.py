def series(n):
    if n == 1:
        return 1
    else:
        return n * series(n-1)

print(series(5))

"""

# Solution

def series(n):
    if n == 1:
        return 1
    else:
        return n * series(n-1)

print(series(5))