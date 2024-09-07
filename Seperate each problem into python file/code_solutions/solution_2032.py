import numpy as np

def matrix_multiply(A, B):
    """
    A : n x m matrix
    B : m x n matrix
    
    Returns the result of A A'B
    """
    # initialize result
    result = np.zeros(A.shape)
    
    # iterate over rows
    for i in range(A.shape[0]):
        # iterate over columns
        for j in range(B.shape[1]):
            # iterate