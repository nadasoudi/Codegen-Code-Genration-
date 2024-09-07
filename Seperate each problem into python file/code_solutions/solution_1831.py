def max_freq_char(string):
    freq = {}
    for char in string:
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1
    max_freq = max(freq.values())
    return max_freq

print(max_freq_char('abcdefghijklmnopqrstuvwxyz'))

"""

def max_freq_char(string):