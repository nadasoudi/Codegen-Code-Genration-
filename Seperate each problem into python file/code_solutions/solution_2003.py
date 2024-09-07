def convert_string_to_datetime(string):
    # Your code here
    return datetime.strptime(string, '%Y-%m-%d %H:%M:%S')

print(convert_string_to_datetime('2021-05-23 12:34:56'))

"""

def convert_string_to_datetime(string):
    # Your code here
    return datetime.strptime(string, '%Y-%m-