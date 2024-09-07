def magic_square(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return magic_square(n-1) + magic_square(n-2)

print(magic_square(5))

"""

# Solution

def magic_square(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return magic_square(n-1)