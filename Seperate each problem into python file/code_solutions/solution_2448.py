def gcd(x, y):
    if x > y:
        x, y = y, x
    while y:
        x, y = y, x % y
    return x

def gcd_recursive(x, y):
    if x > y:
        x, y = y, x
    if x == 0:
        return y
    return gcd_recursive(x % y, y)

def gcd_iterative(x, y):
    while x!= 0