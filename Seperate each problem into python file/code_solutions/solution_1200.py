import numpy as np

a = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])

axis = 1

def weighted_average(a, axis):
    """
    Compute the weighted average along the specified axis.
    
    Parameters
    ----------
    a : array_like
        Array containing data to be averaged.
    axis : int
        Axis along