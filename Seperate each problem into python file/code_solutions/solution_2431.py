def generate_gray_code(n):
    if n == 0:
        return []
    else:
        return generate_gray_code(n-1) + [n]

def generate_gray_code_recursive(n):
    if n == 0:
        return []
    else:
        return generate_gray_code_recursive(n-1) + [n] + generate_gray_code_recursive(n-1)

def generate_gray_code_recursive_2(