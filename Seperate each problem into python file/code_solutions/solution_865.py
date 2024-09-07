def get_frequency(list):
    freq = {}
    for i in list:
        if i in freq:
            freq[i] += 1
        else:
            freq[i] = 1
    return freq

print(get_frequency([1,2,3,4,5,6,7,8,9,10]))

"""

def get_frequency(list):
    freq = {}
    for i in list:
        if