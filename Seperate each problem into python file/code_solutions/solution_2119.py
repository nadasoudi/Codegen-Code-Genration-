class MyClass:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"MyClass object: {self.name} is {self.age}"

    def __repr__(self):
        return f"MyClass object: {self.name} is {self.age}"

    def __eq__(self, other):
        return self.name == other.name and self.age == other.age