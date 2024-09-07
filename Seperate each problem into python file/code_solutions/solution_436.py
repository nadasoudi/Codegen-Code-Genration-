import json

def extract_key_value(dictionary):
    for key, value in dictionary.items():
        print(key, value)

dictionary = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

extract_key_value(dictionary)

# Output:
# name
# age
# city

# Expected Output:
# name
# age
# city

#