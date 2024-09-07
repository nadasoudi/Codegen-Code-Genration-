import math

def remove_even(lst):
    for i in range(len(lst)):
        if lst[i] % 2 == 0:
            lst.remove(lst[i])
    return lst

print(remove_even([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))

# Output: [1, 3, 5, 7, 9]

# Time complexity: O(