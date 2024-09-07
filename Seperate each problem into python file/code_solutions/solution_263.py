def combinations(n, arr):
    if n == 1:
        return [arr]
    else:
        return [arr] + combinations(n-1, arr[:-1])

print(combinations(5, [1, 2, 3, 4, 5]))

"""

def combinations(n, arr):
    if n == 1:
        return [arr]
    else:
        return [arr] + combinations(n-1, arr