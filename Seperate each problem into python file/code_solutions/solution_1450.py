def solution(arr, x):
    for i in range(len(arr)):
        if arr[i] > x:
            return i
    return -1

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
x = 6
print(solution(arr, x))

"""

def solution(arr, x):
    for i in range(len(arr)):
        if arr[i