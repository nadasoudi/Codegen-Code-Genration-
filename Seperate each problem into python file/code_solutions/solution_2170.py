import collections

def extract_k_digit_elements(s):
    return tuple(s[i:i+10] for i in range(0, len(s), 10))

def extract_k_digit_elements_2(s):
    return tuple(s[i:i+10] for i in range(0, len(s), 10))

def extract_k_digit_elements_3(s):
    return tuple(s[i:i+10] for i in