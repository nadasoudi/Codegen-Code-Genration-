def remove_consecutive_k_elements(arr, k):
    # Write your code here
    if len(arr) < k:
        return arr
    else:
        return remove_consecutive_k_elements(arr[1:], k) + [arr[0]] + remove_consecutive_k_elements(arr[1:], k)

# Driver Code
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]