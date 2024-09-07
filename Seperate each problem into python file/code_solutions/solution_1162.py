def count_sublists(arr, element):
    count = 0
    for i in range(len(arr)):
        if arr[i] == element:
            count += 1
    return count

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
element = 5
print(count_sublists(arr, element))

"""

def count_sublists(arr, element):
    count = 0
    for i