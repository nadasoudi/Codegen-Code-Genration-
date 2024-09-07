def get_lower_upper_mixed_case(string):
    lower_mixed_case = []
    upper_mixed_case = []
    for i in string:
        if i.islower():
            lower_mixed_case.append(i)
        elif i.isupper():
            upper_mixed_case.append(i)
    return lower_mixed_case, upper_mixed_case

print(get_lower_upper