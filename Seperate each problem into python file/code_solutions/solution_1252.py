def permutations(n):
    if n == 1:
        return [[1]]
    else:
        permutations = []
        for i in range(1, n+1):
            for j in range(i, n+1):
                permutations.append([i, j])
        return permutations

print(permutations(5))

"""

# Solution:

def permutations(n):
    if