def gcd(x, y):
    if x > y:
        x, y = y, x
    while y:
        x, y = y, x % y
    return x

print(gcd(12, 24))

# Output:
# 7
# Output:
# 7
# Output:
# 7
# Output:
# 7
# Output:
# 7
# Output:
# 7
# Output:
# 7