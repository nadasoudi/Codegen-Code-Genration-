def bitonic_sort(arr):
    # Write your code here
    arr.sort()
    for i in range(len(arr)):
        if arr[i] > arr[i+1]:
            arr[i], arr[i+1] = arr[i+1], arr[i]
    return arr

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(bitonic_sort(arr))

"""