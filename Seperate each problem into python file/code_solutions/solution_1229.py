def get_dict(obj):
    return {
        "name": obj.name,
        "age": obj.age,
        "gender": obj.gender
    }

obj = Person("John", 36, "Male")
print(get_dict(obj))

"""

# Solution:

def get_dict(obj):
    return {
        "name": obj.name,
        "age": obj.age,
        "gender": obj.gender
    }