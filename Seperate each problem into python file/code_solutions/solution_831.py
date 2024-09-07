def remove_key_value_pairs(dictionaries):
    for i in dictionaries:
        for j in i:
            if j in dictionaries[i]:
                dictionaries[i].remove(j)
    return dictionaries

dictionaries = [
    {'name': 'John', 'age': 30, 'city': 'San Francisco'},
    {'name': 'Mary', 'age': 25, 'city': 'Los Angeles'},
    {'