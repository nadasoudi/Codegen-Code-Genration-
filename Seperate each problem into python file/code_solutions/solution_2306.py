import random

def find_missing_values(list1, list2):
    list1.sort()
    list2.sort()
    missing_values = []
    for i in range(len(list1)):
        if list1[i] not in list2:
            missing_values.append(list1[i])
    return missing_values

def find_additional_values(list1, list2):
    list1.sort()
    list2.sort()