import random

def generate_random_number():
    random_number = random.randint(1, 20)
    return random_number

def append_to_list(list_to_append, random_number):
    list_to_append.append(random_number)

def main():
    list_to_append = []
    for i in range(1, 21):
        random_number = generate_random_number()
        append_to_list(