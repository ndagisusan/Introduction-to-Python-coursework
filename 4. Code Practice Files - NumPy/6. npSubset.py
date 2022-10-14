# NumPy Subsetting
length_dim = [1.1, 20.5, 53.6, 26.7, 89.4]  # Length in metres

import numpy as np
np_length = np.array(length_dim)

print(np_length[1])

print(np_length > 25) # Bool values

print(np_length[np_length > 25]) #Actual values