import collections

def removeDuplicates(arr):
    # create a set to store unique elements
    unique_elements = set(arr)
    # create a new array to store the unique elements
    new_arr = []
    # iterate through the array
    for i in arr:
        # if the element is not in the set, add it to the new array
        if i not in unique_elements:
            new_arr.append(i)