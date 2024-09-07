def duplicate_element(arr):
    for i in range(len(arr)):
        if arr[i] == arr[i]:
            return True
    return False

arr = [1,2,3,1,2,3,4,3,2,4,5,6,7,8,9,9,9,9,9,9,9,9,