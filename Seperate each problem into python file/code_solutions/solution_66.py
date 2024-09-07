def first_element_satisfying_function(lst):
    for i in range(len(lst)):
        if lst[i] == first_element_satisfying_function(lst[:i]):
            return lst[i]
    return -1

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(first_element_satisfying_function