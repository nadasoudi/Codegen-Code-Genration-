import json

d = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

with open("my_json.json", "w") as f:
    json.dump(d, f, indent=4)

# Output:
# {
#   "name": "John",
#   "age": 30,
#   "city": "New York"
# }

# Python program to store a given dictionary in