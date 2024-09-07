def kth_largest(arr, n, k):
    return arr[k-1]

def kth_smallest(arr, n, k):
    return arr[n-k]

def kth_largest_and_smallest(arr, n, k):
    return kth_largest(arr, n, k), kth_smallest(arr, n, k)

def kth_largest_and_smallest_recursive(arr, n, k):
    if n == 0 or k