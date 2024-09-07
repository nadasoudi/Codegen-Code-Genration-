def remove_leading_zeros(ip):
    # your code goes here
    return ip.lstrip('0')

print(remove_leading_zeros('127.0.0.1'))
print(remove_leading_zeros('255.255.255.255'))
print(remove_leading_zeros('255.255.255.255.255'))
print(remove_leading_zeros('255.255.255.255.255.255'))
print(