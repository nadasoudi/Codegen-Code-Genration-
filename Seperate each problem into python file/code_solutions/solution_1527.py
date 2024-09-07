def insert_before(list, element):
    for i in range(len(list)):
        list[i] = list[i] + element
    return list

print(insert_before([1, 2, 3, 4, 5], 6))

"""

def insert_before(list, element):
    for i in range(len(list)):
        list[i] = list[i] + element
    return list

print(insert_before([1, 2