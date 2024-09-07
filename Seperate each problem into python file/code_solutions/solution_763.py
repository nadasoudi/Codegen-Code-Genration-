import numpy as np

A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

eigenvalues, eigenvectors = np.linalg.eig(A)

print("Eigenvalues: ", eigenvalues)
print("Eigenvectors: ", eigenvectors)

"""

# Solution:

import numpy as np

A = np