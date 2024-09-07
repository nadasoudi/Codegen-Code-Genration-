def create_list(lst):
    return [[i,j] for i in lst for j in lst]

lst = [[1,2,3],[4,5,6],[7,8,9]]
print(create_list(lst))

"""

def create_list(lst):
    return [[i,j] for i in lst for j in lst]

lst = [[1,2,3],[4,5,6