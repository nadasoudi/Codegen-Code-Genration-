def power(x, y):
    if y == 0:
        return 1
    elif y % 2 == 0:
        return x * power(x, y // 2)
    else:
        return x * power(x, y // 2) * x

print(power(2, 4))

"""

def power(x, y):
    if y == 0:
        return 1
    elif y % 2 == 0:
        return x * power(x, y //