def swap_elements(list1, list2):
    list1[0], list1[1] = list1[1], list1[0]
    list2[0], list2[1] = list2[1], list2[0]
    return list1, list2

list1 = ["a", "b", "c"]
list2 = ["d", "e", "f"]

print(swap_elements(list1, list2))

"""

def swap_e