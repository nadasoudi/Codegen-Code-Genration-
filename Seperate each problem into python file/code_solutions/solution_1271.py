import numpy as np

A = np.array([[1, 2, 3, 4, 5],
              [6, 7, 8, 9, 10],
              [11, 12, 13, 14, 15],
              [16, 17, 18, 19, 20]])

print(np.linalg.cond(A))

"""

# Solution

import numpy as np

A = np.array([[1, 2, 3, 4, 5],