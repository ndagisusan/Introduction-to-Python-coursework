import numpy as np

a = [1, 2, 3, 4, 5] #List data type - mutable
print(type(a))

b = (1, 2, 3, 4, 5) #Tuple data type - immutable
print(type(b))

c = np.array(a)
d = np.array(b)

print(type(c))