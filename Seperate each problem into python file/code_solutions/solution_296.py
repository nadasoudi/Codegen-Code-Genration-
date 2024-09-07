def remove_first(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            arr.pop(i)
    return arr

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
x = 5
print(remove_first(arr, x))

"""

def remove_first(arr, x):
    for i in range(len(arr)):