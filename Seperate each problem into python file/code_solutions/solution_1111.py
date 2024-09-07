def sort_by_length(lst):
    lst.sort(key=len)
    return lst

lst = [[1,2,3,4,5],[1,2,3,4,5],[1,2,3,4,5],[1,2,3,4,5]]
print(sort_by_length(lst))

"""

def sort_by_length(lst):
    lst.sort(key=len)