from array import *

# Create an array from a list of integers
num_array = array('i', range(1, 10))
print("num_array before append()/extend(): {}".format(num_array))

# Add one elements using the append() method
num_array.append(99)
print("num_array after applying append(): {}".format(num_array))

# Add multiple elements using extend() methods
num_array.extend(range(20, 25)) 
print("num_array after applying extend(): {}".format(num_array))
This program yields the following:
