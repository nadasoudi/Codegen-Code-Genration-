def gnome_sort(arr):
    for i in range(len(arr)):
        for j in range(i, len(arr)):
            if arr[j] < arr[i]:
                arr[i], arr[j] = arr[j], arr[i]
    return arr

arr = [10, 4, 2, 5, 8, 9, 1, 7, 6, 3]
print(gnome_sort(arr))

"""

def gnome_sort(arr):
    for