import random

def random_choice(lst):
    return random.choice(lst)

def random_set(lst):
    return set(random.sample(lst, k=len(lst)))

def random_dict(lst):
    return dict(random.sample(lst, k=2))

def random_file(dir):
    return open(dir, 'r').read