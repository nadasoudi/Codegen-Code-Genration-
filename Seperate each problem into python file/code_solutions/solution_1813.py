import json
import csv

def main():
    # Open the JSON file
    with open('/Users/soumya/Desktop/Python/JSON_to_CSV.json') as file:
        data = json.load(file)
    # Iterate through the data and print each key and value
    for key, value in data.items():
        print(key, value)

if __name__ == '__main__':
    main()

# Output:
# 1
# 2
# 3