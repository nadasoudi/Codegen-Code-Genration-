def convert_to_binary(num):
    binary_list = []
    while num > 0:
        binary_list.append(num % 2)
        num = num // 2
    return binary_list

num = int(input("Enter a decimal number: "))
print(convert_to_binary(num))

"""

def convert_to_binary(num):
    binary_list = []
    while num > 0:
        binary_list.append(num %