import numpy as np

def factor(arr):
    # compute singular values
    s = np.linalg.svd(arr, compute_uv=False)
    # compute singular vectors
    u, s, v = s[0], s[1], s[2]
    # compute factor
    return np.dot(u, v)

arr = np.array([[1, 2, 3], [4, 5, 6], [7,