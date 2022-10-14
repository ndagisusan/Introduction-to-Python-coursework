# List Comprehension Example 1

from random import random
size_of_vector = 10     # Don’t use magic numbers
# Magic numbers are numbers with special, hardcoded semantics that appear in code but do not have any meaning or explanation.

# Print random numbers to 2 dp in a specified range in a list
# Without using list comprehension: FOR LOOP
numbers = []
for i in range(size_of_vector):
    numbers.append(round(random(), 2))
    
print(numbers)

# Using LIST COMPREHENSION
numbers = [round(random(), 2) for i in range(size_of_vector)]
print(numbers)      # Prints another random list of 10 numbers dur to the random function