import numpy as np

a = np.random.randint(0,10,(4,4))
print(a)

b = np.random.randint(0,10,(4,4))
print(b)

c = np.concatenate((a,b),axis=1)
print(c)

d = np.concatenate((a,b),axis=