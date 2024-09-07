import numpy as np

def searchsorted(a, v):
    """
    Find the indices where element v should be inserted in a sorted array.

    Parameters
    ----------
    a : ndarray
        Input array.
    v : float
        Value to insert into a.

    Returns
    -------
    indices : ndarray of ints
        Indices of elements to insert.

    See Also
    --------
    searchsorted_left

    """
    ind = (a == v).non