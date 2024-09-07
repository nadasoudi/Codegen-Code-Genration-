import json

with open('/Users/srinivasan/Desktop/Python/json_to_dict.json') as f:
    data = json.load(f)

print(type(data))

print(data['a'])

print(data['a']['b'])

print(data['a']['b']['c'])

print(data['a']['b']['c']['d'])

print(data['a']['b'][