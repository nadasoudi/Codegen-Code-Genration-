def pattern(n):
    if n == 1:
        return '*'
    else:
        return pattern(n-1) + '*' + pattern(n-2)

print(pattern(3))

"""

# Solution:

def pattern(n):
    if n == 1:
        return '*'
    else:
        return pattern(n-1) + '*' + pattern(n-2)

print(pattern(3))