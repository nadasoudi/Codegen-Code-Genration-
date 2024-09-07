import json

def convert_json_to_string(json_data):
    return json.dumps(json_data)

def main():
    json_data = {
        "name": "John",
        "age": 30,
        "city": "New York"
    }
    print(convert_json_to_string(json_data))

if __name__ == "__main__":
    main()

# OUTPUT:
# {
#   "name": "John",