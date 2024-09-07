def is_method(obj):
    if type(obj) == types.MethodType:
        return True
    else:
        return False

print(is_method(1))
print(is_method(1.0))
print(is_method(1.0 + 2.0))
print(is_method(1.0 + 2.0 + 3.0))
print(is_method(1.0 + 2.0 +