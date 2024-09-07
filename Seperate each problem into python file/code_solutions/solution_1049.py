import numpy as np

a = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

if all(a):
    print("All elements evaluate to True")
else:
    print("Some elements evaluate to False")

# Output

# All elements evaluate to True
# Some elements evaluate to False