def odd_frequency_characters(string):
    odd_characters = []
    for char in string:
        if char.isalpha():
            odd_characters.append(char)
    return ''.join(odd_characters)

print(odd_frequency_characters('Python'))

"""

def odd_frequency_characters(string):
    odd_characters = []
    for char in string:
        if char.isalpha():
            odd_characters.append(char)