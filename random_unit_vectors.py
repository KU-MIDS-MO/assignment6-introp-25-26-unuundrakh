import numpy as np

def random_unit_vectors(num_vectors, dim):
    # generate random vectors
    M = np.random.randn(num_vectors, dim) 
    # normalise each vector
    normalised_vectors = np.array([normalise_vector(vec) for vec in M])
    # print the normalised vectors
    return normalised_vectors

    
def normalise_vector(vector):
    # calculate the l2 norm of the vector
    l2_norm = np.linalg.norm(vector)
    # check to avoid division by zero
    if l2_norm == 0:
        # raise an error for zero vector
        raise ValueError ("Cannot normalise a zero vector")
        # correct normalization formula
    return vector / l2_norm
       
# store the normalised vectors
vectors = random_unit_vectors(5, 3)
# print the normalised vectors
print("Normalised unit vecotrs:\n", vectors)
  

# unit vector of 1
    
#   Write a function:
         
#`random_unit_vectors(num_vectors, dim)`
#     that:
#     a)creates a matrix M of shape (num_vectors, dim)using;#

#     M = np.random.randn(num_vectors, dim)
#
#     b)normalizes each row so it has Euclidean norm 1,

#     and c)returns the resulting matrix as a NumPy array.
