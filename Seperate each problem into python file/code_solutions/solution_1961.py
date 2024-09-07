def consecutive_kth_column_difference(arr, k):
    # Write your code here
    return arr[k] - arr[k - 1]

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
k = 3
print(consecutive_kth_column_difference(arr, k))

"""

def consecutive_kth_column_difference(arr, k):
    # Write your code here