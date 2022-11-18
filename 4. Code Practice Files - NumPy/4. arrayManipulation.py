# NumPy array manipulation
length_dim = [1.1, 20.5, 53.6, 26.7, 89.4]  # Length in metres
width = [10.23, 28.15, 24.6, 33.58, 54] # Width in metres

import numpy as np    # Can be put anywhere in the program once you require to use it
np_length = np.array(length_dim) # Create a NumPy array from a Python list
np_width = np.array(width)

np_area = np_length * np_width
print("Area: ", np_area)
print(type(np_area), "\n")


# EXAMPLE 2 - Add 2 arrays
np_sum_dim = np_length + np_width
print(np_sum_dim) # Add the vector values together. Array of same size


# EXAMPLE 3
# Convert length in m to cm
np_length_cm = np.array(length_dim) * 100
print(np_length_cm)
# OR
# np_length_cm = np_length * 100
# print(np_length_cm)
