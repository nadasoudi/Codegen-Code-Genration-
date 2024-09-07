def odd_numbers(input_list):
    for i in range(len(input_list)):
        if input_list[i] % 2 == 1:
            print(input_list[i])

input_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
odd_numbers(input_list)

"""

def odd_numbers(input_list):
    for i in range(len(input_list)):
        if