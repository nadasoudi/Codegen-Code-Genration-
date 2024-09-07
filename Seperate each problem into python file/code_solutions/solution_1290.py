def radixSort(arr):
    # Write your code here
    for i in range(len(arr)):
        for j in range(len(arr)):
            if arr[j] >= arr[i]:
                arr[j], arr[i] = arr[i], arr[j]
    return arr

# Driver code
arr = [10, 4, 9, 2, 5, 8, 3, 1, 6, 7]
print(radixSort(arr))