def bogo_sort(lst):
    for i in range(len(lst)):
        random.shuffle(lst)
    return lst

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(bogo_sort(lst))

"""

# Time complexity: O(n^2)
# Space Complexity: O(1)

def bogo_sort(lst):