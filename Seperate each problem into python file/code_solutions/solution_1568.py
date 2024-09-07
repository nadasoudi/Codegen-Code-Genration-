import numpy as np

a = np.array([[True, False, True],
              [False, False, True],
              [True, True, False]])

print(np.any(a, axis=0))

# OUTPUT:
# True
# True
# True
# True
# True
# True
# True
# True
# True
# True
# True
# True
# True
# True
# True
# True
#