import numpy as np

a = np.array([1, 2, 3, 4, 5])

a.flags.writeable = False

print(a)

a.flags.writeable = True

print(a)

a.flags.writeable = False

print(a)

a.flags.writeable = True

print(a)

a.flags.writeable = False

print(a)

a.flags.writeable = True

print