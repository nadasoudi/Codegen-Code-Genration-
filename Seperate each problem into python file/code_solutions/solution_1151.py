def next_smallest(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    if n == 3:
        return 3
    if n % 2 == 0:
        return next_smallest(n//2)
    else:
        return next_smallest(n-1)

print(next_smallest(int(input())))

"""

def next_smallest(n):
    if n ==