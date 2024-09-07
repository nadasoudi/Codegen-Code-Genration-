def removeDuplicates(arr):
    # Write your code here
    newArr = []
    for i in range(len(arr)):
        if arr[i] not in newArr:
            newArr.append(arr[i])
    return newArr

# Driver code
arr = [1, 1, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8