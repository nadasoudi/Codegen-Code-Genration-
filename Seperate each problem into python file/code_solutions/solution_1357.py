python solution.py

"""

# Solution 1

def find_keys_with_value(d, value):
    """
    :param d: dictionary
    :param value: value to be searched
    :return: list of keys with value
    """
    return [key for key, value in d.items() if value == value and key!= value]

# Solution 2

def find_keys_with_value(d, value):
    """
    :