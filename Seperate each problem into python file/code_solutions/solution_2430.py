def hex_to_dec(num):
    if num == 0:
        return 0
    else:
        return num * 16 + hex_to_dec(num // 16)

def dec_to_hex(num):
    if num == 0:
        return 0
    else:
        return num * 16 + dec_to_hex(num // 16)

def main():
    num = int(input("Enter a decimal number: "))
    print("Hexadecimal representation of