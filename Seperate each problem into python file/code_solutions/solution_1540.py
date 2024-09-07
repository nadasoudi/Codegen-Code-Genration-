import itertools

def permutations(n):
    return list(itertools.permutations(range(1, n+1)))

print(permutations(5))

"""

# Solution 1

def permutations(n):
    if n == 1:
        return [[1]]
    else:
        return [list(itertools.permutations(range(1, n+1))) for i in range(n)]

print(permutations(5))