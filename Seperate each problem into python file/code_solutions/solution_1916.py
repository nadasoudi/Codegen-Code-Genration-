import json

with open('data.json') as f:
    data = json.load(f)

# Solution 1:
# print(type(data))
# print(data)

# Solution 2:
# print(type(data['data']))
# print(data['data'])

# Solution 3:
# print(type(data['data']['data']))
# print(data['data']['data'])

# Solution 4:
# print(type(data['data