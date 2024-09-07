"""

import math
import sys

def find_strongest_neighbour(arr, n):
    # Write your code here
    max_val = -math.inf
    max_index = -1
    for i in range(n):
        if arr[i] > max_val:
            max_val = arr[i]
            max_index = i
    return max_index

if __name__ == '__main__':
    n = int(input())
    arr =