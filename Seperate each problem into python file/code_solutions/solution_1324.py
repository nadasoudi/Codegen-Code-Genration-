def lcm(x, y):
    return (x * y) // gcd(x, y)

def gcd(x, y):
    while y:
        x, y = y, x % y
    return x

print(lcm(12, 24))

# Output: 24
# Explanation: The L.C.M. is the smallest positive integer that is evenly divisible by both 12 and 24.

# Input Format
# The first