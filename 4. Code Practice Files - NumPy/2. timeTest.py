import numpy as np
import time
size_of_vec = 1000000

def pure_python_version(): #LISTS
    start = time.time()
    X = range(size_of_vec) # X = [0, 1, 2 , 3, ..., 999999]
    Y = range(size_of_vec) # Y = [0, 1, 2 , 3, ..., 999999]
    Z = [X[i] + Y[i] for i in range(len(X)) ] #list; Z = [0, 2, 4, 6,....]
    return time.time() - start


def numpy_version(): #NumPy arrays
    start = time.time()
    X = np.arange(size_of_vec)  # X = [0, 1, 2 , 3, ..., 999999]
    Y = np.arange(size_of_vec) # Y = [0, 1, 2 , 3, ..., 999999]
    Z = X + Y #an array; Z = [0, 2, 4, 6,....]
    return time.time() - start

t1 = pure_python_version()
t2 = numpy_version()

print("T1(list): ", t1, "\t T2(array): ", t2)
print("Numpy is in this example " + str(t1/t2) + " faster!")