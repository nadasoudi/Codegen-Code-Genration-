python solution.py

"""

import numpy as np

def get_indices(arr, key):
    """
    Returns the indices of the elements of arr that match the key.
    
    Parameters
    ----------
    arr : ndarray
        The array to search.
    key : function
        The key function to use to compare the elements.
    
    Returns
    -------
    indices : ndarray
        The indices of the elements of arr that