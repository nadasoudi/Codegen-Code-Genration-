def common_char(a, b):
    common_char = []
    for i in range(len(a)):
        if a[i] in b:
            common_char.append(a[i])
    return common_char

a = "abcd"
b = "abcd"
print(common_char(a, b))

"""

# Solution:

def