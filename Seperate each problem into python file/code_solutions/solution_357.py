def is_generator(obj):
    if type(obj) == types.GeneratorType:
        return True
    else:
        return False

print(is_generator(lambda: 1))
print(is_generator(lambda: 2))
print(is_generator(lambda: 3))
print(is_generator(lambda: 4))
print(is_generator(lambda: 5))
print(is_generator(lambda: