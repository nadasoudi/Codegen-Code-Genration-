import numpy as np

x = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

if x[x > 5] == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
    print("Yes")
else:
    print("No")

"""

# Solution

import numpy as np

x = np.array([1, 2, 3, 4, 5, 6, 7