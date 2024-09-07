import numpy as np

a = np.array([[1, 2, 3],
              [4, 5, 6]])

print(a.moveaxis(0, 2))

"""

# Solution

# numpy.moveaxis() function
#
# Given an array and a destination axis, move the array to the given axis.
#
# For example, move axis 0 to the first position, move axis 1 to the second position,
# and so on.
#
# Note that the order of the