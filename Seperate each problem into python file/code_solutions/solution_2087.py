def binary_insertion_sort(arr):
    for i in range(1, len(arr)):
        j = i
        while j > 0 and arr[j] < arr[j-1]:
            arr[j], arr[j-1] = arr[j-1], arr[j]
            j -= 1
    return arr

arr = [12, 11, 13, 5, 6, 7]
print(binary_insertion_sort(arr))

"""

def binary_insertion_