def bitonic_sort(arr):
    # Write your code here
    arr.sort()
    for i in range(len(arr)):
        if arr[i] > arr[i+1]:
            arr[i], arr[i+1] = arr[i+1], arr[i]
    return arr

arr = [1, 5, 2, 4, 3, 6, 7, 8, 9, 10]
print(bitonic_sort(arr))

"""

"""

def bitonic