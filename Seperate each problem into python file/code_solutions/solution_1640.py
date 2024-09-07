import numpy as np

def encode(arr):
    encoded = np.zeros(len(arr), dtype=int)
    for i in range(len(arr)):
        encoded[i] = arr[i]
    return encoded

def decode(arr):
    decoded = np.zeros(len(arr), dtype=int)
    for i in range(len(arr)):
        decoded[i] =