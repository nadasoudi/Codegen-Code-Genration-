def match_key_values(dict1, dict2):
    for key in dict1:
        if key in dict2:
            if dict1[key] == dict2[key]:
                print(f"{key} is a match")
            else:
                print(f"{key} is not a match")
        else:
            print(f"{key} is not a match")

if __name__ == '__main__':
    dict1 = {'a': 1