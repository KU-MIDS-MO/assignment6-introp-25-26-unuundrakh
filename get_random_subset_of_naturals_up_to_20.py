import numpy as np

def get_random_subset_of_naturals_up_to_20():
    n = np.random.randint(0, 2**20)
    bits = np.array(list(np.binary_repr(n, width=20)), dtype=int)
    return np.arange(1, 21) [bits == 1]

     



