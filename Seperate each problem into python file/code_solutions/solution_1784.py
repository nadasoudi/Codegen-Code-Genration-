import numpy as np

def geometric(n):
    """
    Returns the geometric sequence of n numbers.
    """
    if n == 0:
        return []
    elif n == 1:
        return [1]
    else:
        return [1 + geometric(n - 1)] + geometric(n - 1)

print(geometric(5))

"""
Output:
[1, 1, 1, 2, 4, 9, 16, 25, 36, 49, 64, 81, 100