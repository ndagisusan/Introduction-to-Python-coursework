# List manipulation
length_dim = [1.1, 20.5, 53.6, 26.7, 89.4]  # Length in metres
width = [10.23, 28.15, 24.6, 33.58, 54] # Width in metres

# area = length_dim * width    # Will this operation be done?
# print("Area: ", area)

# OPTION 1
area = [] # Initialize empty list
for i in range(len(length_dim)): # Assumes lists of equal length
    l = length_dim[i]
    w = width[i]
    area.append(l * w)
print("Area: ", area)

# OPTION 2 - List comprehension of OPTION 1
# area = [length_dim[i] * width[i] for i in range(len(length_dim)) ] # Assumes lists of equal length 
# print("Area: ", area)

# OPTION 3
# area = []
# for l, w in zip(length_dim, width): #Lists can be of differnt lengths
# 	area.append(l * w)
# print("Area: ", area)


# EXAMPLE 2 - Adding 2 lists
sum_dim = length_dim + width
print(sum_dim) # Append the 2 lists together. List is now longer


# EXAMPLE 3
# Convert length in m to cm
length_cm = [l * 100 for l in length_dim]
print(length_cm)


