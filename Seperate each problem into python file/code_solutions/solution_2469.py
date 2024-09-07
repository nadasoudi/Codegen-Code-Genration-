def sum_series(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return sum_series(n-1) + sum_series(n-2) + sum_series(n-3)

print(sum_series(5))

"""

# Solution

def sum_series(n):
    if n == 0:
        return 0
    elif n ==