import collections

def most_common(text):
    # create a dictionary to store the count of each character
    counts = collections.Counter(text)
    # sort the dictionary by the values
    counts = sorted(counts.items(), key=lambda x: x[1], reverse=True)
    # return the top 10 most common characters
    return counts[:10]

print(most_common('abcdefghijklmnopqrstuvwxyz