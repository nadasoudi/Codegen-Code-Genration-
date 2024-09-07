def sort_by_length(lst):
    return sorted(lst, key=len)

lst = [[1,2,3,4,5], [2,4,6,8,10], [3,6,9,12,15], [1,5,7,9,11]]
print(sort_by_length(lst))

"""

# Solution:

def sort_by_length(lst):
    return sorted(l