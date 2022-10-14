# MATPLOTLIB - LISTS
import matplotlib.pyplot as plt

x = [0, 2, 4, 6, 8, 10]
y = [0, 10, 15, 26, 46, 50]

# Labels
plt.xlabel("Range x")
plt.ylabel("Range y")
plt.title("Range y against Range x")

# Different plots - plot, scatter, hist
plt.plot(x, y)    # Line graph - The labels above apply for this plot only
plt.show() 

plt.scatter(x, y)             # Scatter graph
plt.show()

plt.hist(x)                   # Histogram: Default bins = 10. Can specify the number of bins using the bins parameter
plt.show()
plt.clf()                     # Clears the current plot


# MATPLOTLIB - NUMPY ARRAY
import matplotlib.pyplot as plt
import numpy as np

x = [0, 2, 4, 6, 8, 10]
y = [0, 10, 15, 26, 46, 50]

np_x = np.array(x)
np_y = np.array(y)

# Labels
plt.xlabel("Range x")
plt.ylabel("Range y")
plt.title("Range y against Range x")

# Different plots - plot, scatter, hist
plt.plot(np_x, np_y, marker="*", c = 'green', alpha = 0.8)    # Line graph - The labels above apply for this plot only
# marker: format can be o or * , c: color, alpha: opacity(Range: 0-1)
plt.show()                          # Displays the plot

plt.scatter(np_x, np_y, marker="*", c = 'purple', alpha = 0.5)             # Scatter graph
plt.show()

plt.hist(np_x)                      # Histogram: Default bins = 10. Can specify the number of bins using the bins parameter
plt.show()
plt.clf()