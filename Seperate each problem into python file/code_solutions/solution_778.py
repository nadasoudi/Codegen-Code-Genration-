def append_same_value(list_of_lists):
    for i in range(len(list_of_lists)):
        list_of_lists[i].append(list_of_lists[i][0])
    return list_of_lists

print(append_same_value([[1,2,3],[4,5,6],[7,8,9]]))

"""

def append_same_value(list_