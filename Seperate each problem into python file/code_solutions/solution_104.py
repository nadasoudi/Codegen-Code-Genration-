def combinations(n, k):
    if n == 0:
        return []
    if n == 1:
        return [[1]]
    if n == 2:
        return [[1, 1]]
    if n == 3:
        return [[1, 1, 1]]
    if n == 4:
        return [[1, 1, 1, 1]]
    if n == 5:
        return [[1, 1, 1, 1, 1]]
    if n == 6:
        return [[