>>> import numpy as np
>>> a = np.array([[1, 2, 3], [4, 5, 6]])
>>> a.diagonal()
array([1, 4, 5, 6])

"""

# Import NumPy
import numpy as np

# Create a NumPy array
a = np.array([[1, 2, 3], [4, 5, 6]])

# Print the diagonal elements of the array
print(a.diagonal())