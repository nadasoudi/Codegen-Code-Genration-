import numpy as np

def is_par(x):
    return x % 2 == 0

def is_par_outlier(x):
    return np.any(is_par(x) == False)

def is_par_outlier_list(x):
    return [is_par(x) == False for x in x]

def is_par_outlier_list_2(x):
    return [is_par(x) == False