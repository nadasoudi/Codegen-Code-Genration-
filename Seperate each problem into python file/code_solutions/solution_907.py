def is_abundant(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return True
    return False

print(is_abundant(12))

"""

def is_abundant(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return True
    return