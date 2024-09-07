def power(x, n):
    if n == 0:
        return 1
    elif n % 2 == 0:
        return x * power(x, n // 2)
    else:
        return x * power(x, n - 1)

print(power(2, 3))

"""

def power(x, n):
    if n == 0:
        return 1
    elif n % 2 == 0:
        return x * power(x, n // 2)
    else: