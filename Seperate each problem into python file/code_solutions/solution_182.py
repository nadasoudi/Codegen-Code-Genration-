def is_perfect(n):
    if n == 1:
        return True
    elif n % 2 == 0:
        return False
    else:
        return is_perfect(n // 2)

print(is_perfect(5))

"""

def is_perfect(n):
    if n == 1:
        return True
    elif n % 2 == 0:
        return False
    else:
        return is_perfect(n // 2)

print(