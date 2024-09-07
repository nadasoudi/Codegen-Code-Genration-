def bisect(a, x, lo, hi):
    if hi < lo:
        return -1
    mid = (lo + hi) // 2
    if a[mid] == x:
        return mid
    elif a[mid] > x:
        return bisect(a, x, lo, mid - 1)
    else:
        return bisect(a, x, mid + 1, hi)

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10