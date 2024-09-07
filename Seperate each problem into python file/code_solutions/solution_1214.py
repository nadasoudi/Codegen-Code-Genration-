python nested_list_elements.py

"""

# Solution 1

def nested_list_elements(ls):
    """
    :type ls: List[List[int]]
    :rtype: List[int]
    """
    result = []
    for i in ls:
        for j in i:
            if j not in result:
                result.append(j)
    return result

# Solution 2

def nested_list_elements