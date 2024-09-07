import numpy as np

np.random.seed(0)

x = np.random.randint(0, 10, 15)
x[x.argmax()] = -1

print(x)

"""

import numpy as np

np.random.seed(0)

x = np.random.randint(0, 10, 15)
x[x.argmax()] = -1

print(x)