def count_occurrences(arr, n):
    count = 0
    for i in range(n):
        if arr[i] == arr[i]:
            count += 1
    return count

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
n = len(arr)
print(count_occurrences(arr, n))

"""

def count_occurrences(arr,