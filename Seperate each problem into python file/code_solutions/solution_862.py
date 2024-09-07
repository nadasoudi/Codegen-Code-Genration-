import math

def rgb_to_hex(r, g, b):
    return '#{:02x}{:02x}{:02x}'.format(r, g, b)

print(rgb_to_hex(255, 0, 0))
print(rgb_to_hex(0, 255, 0))
print(rgb_to_hex(0, 0, 255))
print(rgb_to_hex(0, 0,