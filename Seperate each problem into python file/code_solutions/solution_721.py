import json

with open('data.json') as f:
    data = json.load(f)

print(data)

# Output:
# {
#   "name": "John",
#   "age": 30,
#   "gender": "Male"
# }

# Create a new JSON file
# with open('data.json', 'w') as f:
#     json.dump(data, f)

# Output:
# {
#