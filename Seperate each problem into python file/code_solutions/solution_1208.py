import random

def generate_random_float():
    return random.uniform(0, 1)

def generate_random_float_within_range(lower_bound, upper_bound):
    return random.uniform(lower_bound, upper_bound)

def generate_random_float_within_range_2(lower_bound, upper_bound):
    return random.uniform(lower_bound, upper_bound