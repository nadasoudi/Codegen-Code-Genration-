def invert_pattern(n):
    if n == 0:
        return " "
    else:
        return invert_pattern(n-1) + "*" + invert_pattern(n-1)

print(invert_pattern(5))

"""

# Solution:

def invert_pattern(n):
    if n == 0:
        return " "
    else:
        return invert_pattern(n-1) + "*" + invert_pattern(