import numpy as np

def roots(p):
    # compute roots of polynomial
    roots = np.roots(p)
    # return roots
    return roots

# test
p = np.array([1, 2, 3, 4])
roots = roots(p)
print(roots)

# test
p = np.array([1, 2, 3, 4])
roots = roots(p)
print(roots)

# test
p = np.array([1