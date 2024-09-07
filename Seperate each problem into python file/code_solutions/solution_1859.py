def binary_search(arr, target):
    if len(arr) == 0:
        return -1
    else:
        mid = len(arr) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            return binary_search(arr[:mid], target)
        else:
            return binary_search(arr[mid + 1:], target)

arr = [1, 2, 3, 4, 5, 6,