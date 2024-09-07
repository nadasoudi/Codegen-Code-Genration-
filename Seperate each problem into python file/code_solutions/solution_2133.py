def nested_dictionary(d):
    for i in d:
        if type(d[i]) == dict:
            print(d[i])
            nested_dictionary(d[i])
        else:
            print(d[i])

d = {'a': 1, 'b': 2, 'c': 3}
nested_dictionary(d)

"""

def nested_dictionary(d):
    for i in d:
        if type(d[i