import numpy as np

def sine(x):
    return np.sin(x)

def cosine(x):
    return np.cos(x)

def tangent(x):
    return np.tan(x)

x = np.arange(0, np.pi, 0.1)

sine_answer = sine(x)
print(sine_answer)

cosine_