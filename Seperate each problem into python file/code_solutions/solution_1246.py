python solution.py

"""

import numpy as np

def solution(d):
    """
    :type d: dict
    :rtype: np.ndarray
    """
    return np.array(list(d.values()))

if __name__ == '__main__':
    d = {'a': 1, 'b': 2, 'c': 3}
    print(solution(d))