def nested_list_elements(lst):
    result = []
    for i in lst:
        if type(i) is list:
            result.extend(nested_list_elements(i))
        else:
            result.append(i)
    return result

lst = [[1,2,3],[4,5,6],[7,8,9]]
print(nested_list_elements(lst))