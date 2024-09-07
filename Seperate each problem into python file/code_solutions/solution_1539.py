import numpy as np

a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

print("Frobenius norm is:", np.linalg.norm(a))
print("Condition number is:", np.linalg.cond(a))

"""

# Solution

import numpy as np

a = np.array([[1, 2, 3], [4