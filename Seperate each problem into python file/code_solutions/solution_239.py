def convert_to_binary(num):
    binary = ''
    while num > 0:
        binary = str(num % 2) + binary
        num = num // 2
    return binary

print(convert_to_binary(5))

"""

def convert_to_binary(num):
    binary = ''
    while num > 0:
        binary = str(num % 2) + binary
        num = num // 2
    return binary

print(convert