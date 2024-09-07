def common_values(str1, str2):
    common_values = []
    for i in range(len(str1)):
        for j in range(len(str2)):
            if str1[i] == str2[j]:
                common_values.append(str1[i])
    return common_values

print(common_values("abcd", "abcd"))

"""

def common_values(str1, str2):
    common_