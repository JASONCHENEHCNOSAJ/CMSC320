import numpy as np
import random

"""
(a) How do you create a Numpy array of zeros with a specific shape?
(b) How do you create a NumPy array of random integers with a specific shape?
(c) How do you calculate the mean of a NumPy array along row axis?
(d) How do you reshape a NumPy array to a specific shape?
(e) How do you concatenate two NumPy arrays vertically?
"""

#(a) How do you create a Numpy array of zeros with a specific shape?
# Ans: You do this by calling np.zeros with the dimensions of the shape as arguments in parenthesis

x = np.zeros((4,5))
print("(A) ", x)

#(b) How do you create a NumPy array of random integers with a specific shape?
# Ans: You do np.random.random() with the dimensions as arguments in parenthesis

y = np.random.random((4,5))
print("(B) ", y)

# (c) How do you calculate the mean of a NumPy array along row axis?
# Ans: you use the np.mean() function passing in the array and specifying the axis as 0 for row and 1 for column as such
# np.mean(x, axis = 0)
 
x = np.random.randint(12,20,(4,5))
print(x)
print("The mean of this array is", np.mean(x,axis=0))

# (d) How do you reshape a NumPy array to a specific shape?
# Ans: This is pretty straightforward. All you do is call np.reshape() and passing in the
# dimensions as arguments

x = np.array(np.random.randint(0,101,(5,5)))
print("The Orig x is", x)
np.reshape(x, (4,5))
print("After reshaping to 4,5, it looks like", x)


#Other Numpy Functions
sdfsdfsdf

#Slicing in Numpy
#You take array slices by adding a colon in the brackets
x = np.arange(12)

#If you want the first z elements of the array, do x[:z]
print("Printing the first 5 elem of arr", x[:5])

#If you want to print incremental values of the array, do x[:arr size:inc]
# This will print indices incrementing by inc, not including the value of arr size,
# In other words, putting x[:12:3] prints [0,3,6,9]. It doesn't include 12 because it only
# goes up until that first argument, but not including.
print("Printing the every 3rd elem of arr", x[:12:3])

""" If you leave that first argument empty like [::3], then it will just print
every 3rd elem of the whole array,"""
print("Printing the every 3rd elem of arr", x[::3])