# Importing the numpy module
import numpy as np

# This is a simple python list
a = [1, 2, 3]
# Converting this to an array
x = np.array(a)
# Creating the same array directly
y = np.array([1, 2, 3])
# Turning an array into a list
b = y.tolist()
# Same list as we started with?
print(a==b)
# Sum of lists a and b
print(a + b)
# Sum of arrays x and y
print(x + y)

"""creating Sequence"""
# Creating a sequence of integers from -5 to 10
x = np.arange(-5, 11)
print(x)