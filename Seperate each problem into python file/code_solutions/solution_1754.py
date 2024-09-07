import numpy as np

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

c = np.cov(a, b)

print(c)

# Output:
[[1.25  0.        ]
 [0.666667  0.333333]
 [0.333333  0.666667]]

"""

import numpy as np

a = np.array([1, 2, 3])