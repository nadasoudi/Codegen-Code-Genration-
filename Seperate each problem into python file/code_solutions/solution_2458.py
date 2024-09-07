def series(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return series(n-1) + series(n-2)

print(series(5))

"""

# Solution

def series(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return series(n-1) + series(n-2)