def reverse_list(lst):
    for i in range(len(lst)):
        lst[i] = lst[i][::-1]
    return lst

lst = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(reverse_list(lst))

"""

# Solution 1

def reverse_list(lst):
    for i in range(len(lst)):