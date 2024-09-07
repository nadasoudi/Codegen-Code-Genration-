def combinations(lst, n):
    if n == 0:
        return [[]]
    else:
        return [item for sublist in combinations(lst, n-1) for item in sublist] + [item for sublist in combinations(lst, n-1) for item in sublist]

print(combinations([1,2,3,4,5],3))

"""

def combinations(lst, n):
    if n == 0: