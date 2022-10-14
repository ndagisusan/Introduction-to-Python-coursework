import numpy as np

# Generating arrays with random values
a = np.zeros(3, int) #Array with zeros
print(a)

b = np.ones(5, int) #Array with ones
print(b)

c = np.empty(1000, int) # Random values
print(c)

d = np.arange(15) # (start, stop, step)
print(d)

# https://pynative.com/python-random-randrange/ 
e = np.random.randint(10, size=(15, 6))
print(e)
