def combinations(n, k):
    if n == k:
        print(n, end=" ")
        return
    else:
        for i in range(1, n + 1):
            combinations(n - i, k)
            print(i, end=" ")

combinations(3, 3)

"""

def combinations(n, k):
    if n == k:
        print(n, end=" ")