import numpy as np

a = np.random.randint(10, size=(2,3))
b = np.random.randint(10, size=(2,3))

print(a == b)

# Output:

[[ True  True  True]
 [False  True  True]
 [False  True  True]]

# Expected output:

[True  True  True]
[False  True  True]
[False  True  True]