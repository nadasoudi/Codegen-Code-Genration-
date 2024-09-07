def minimum(arr):
    min = arr[0][0]
    for i in range(1, len(arr)):
        for j in range(len(arr[i])):
            if arr[i][j] < min:
                min = arr[i][j]
    return min

print(minimum([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]))

"""

def minimum(arr):
    min = arr[0][