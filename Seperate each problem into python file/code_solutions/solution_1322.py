def get_triangle(a, b, c):
    if a == b == c:
        return a
    elif a == b or b == c or a == c:
        return b
    else:
        return get_triangle(a, b, c - 1) + get_triangle(a, b - 1, c - 1) + get_triangle(a - 1, b, c - 1) + get_triangle(a - 1, b -