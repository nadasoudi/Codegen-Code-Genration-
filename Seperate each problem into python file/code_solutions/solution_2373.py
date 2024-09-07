import numpy as np

def var(x):
    return np.var(x)

def mean(x):
    return np.mean(x)

def std(x):
    return np.std(x)

def test_var():
    assert var([1, 2, 3]) == 3
    assert var([1, 2, 3, 4]) == 4
    assert var([1, 2, 3, 4, 5]) == 5
    assert var([1, 2, 3, 4, 5, 6