def remove_multiple_empty_spaces(list):
    for i in range(len(list)):
        if list[i] == " ":
            list.remove(list[i])
    return list

print(remove_multiple_empty_spaces([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))

"""

def remove_multiple_empty_spaces(list):
    for i in range(len(list)):