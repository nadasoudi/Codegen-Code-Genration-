import json

def dict_to_json(d):
    return json.dumps(d)

def json_to_dict(s):
    return json.loads(s)

def main():
    d = {'a': 1, 'b': 2, 'c': 3}
    print(dict_to_json(d))
    print(json_to_dict(dict_to_json(d)))

if __name__ == '__main__':
    main()