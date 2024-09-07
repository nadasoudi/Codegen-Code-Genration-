def remove_item(arr, item):
    for i in range(len(arr)):
        if arr[i] == item:
            arr.pop(i)
    return arr

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
item = 6
print(remove_item(arr, item))

"""

def remove_item(arr, item):
    for i in range(len(arr)):