def combinations(n, k):
    if k == 0:
        return [[]]
    else:
        return combinations(n, k-1) + [[n, k]]

n = int(input())
k = int(input())
print(combinations(n, k))

# Solution:

def combinations(n, k):
    if k == 0:
        return [[]]
    else:
        return [[n] + list(combinations(n, k-1))