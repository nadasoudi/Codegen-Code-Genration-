import numpy as np

arr = np.array([[1, 2, 3, 4],
                [5, 6, 7, 8],
                [9, 10, 11, 12]])

arr = np.pad(arr, (2, 2), 'constant', constant_values=(0, 0))

arr = np.pad(arr, (2, 2), 'edge')

arr = np.pad(arr, (2, 2), 'edge