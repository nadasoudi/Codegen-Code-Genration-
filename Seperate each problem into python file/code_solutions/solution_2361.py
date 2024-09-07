def solution(arr):
    for i in range(len(arr)):
        if arr[i] in arr:
            return arr.index(arr[i])
    return -1

#Provide different values for arr and test your program
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(solution(arr))

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(solution(arr