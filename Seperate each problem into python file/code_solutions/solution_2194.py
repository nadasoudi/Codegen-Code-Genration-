def convert_unknown_format_string_to_datetime(unknown_format_string):
    # Your code here
    return datetime.strptime(unknown_format_string, '%Y-%m-%d %H:%M:%S')

print(convert_unknown_format_string_to_datetime('2021-01-01T00:00:00Z'))

"""

# Solution

def convert_unknown_format_string_to_datetime(unknown