def create_dict(key_list):
    dict = {}
    for key in key_list:
        dict[key] = []
    return dict

def group_key_value(dict):
    for key, value in dict.items():
        print(key, value)

if __name__ == '__main__':
    key_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', '