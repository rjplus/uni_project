#!/usr/bin/env python
# coding: utf-8

# # NumPy
# 
# Programming in Python
# 
# School of Computer Science, University of St Andrews

# NumPy is a Python library that adds support for **Array Programming** to the language.

# Array programming is a high-level programminng model where operations are applied to many data values simultaneously.

# To achive this, we bundle many data values into tables of elements that all have the same type. We call these **Arrays**!

# Array programming has a long history in computer science, going back to 1960s. Languages that support Array programming include:
# - APL
# - Matlab
# - Julia

# ## Benefits of Array programming vs. Scalar Programming

# **Concision** - Often allows for transformations on data to be written as short expressions that retain their readability.

# **Parallel** - Better suited to implicit parallellisation via SIMD instructions in modern CPU cores.

# **Performance** - Improved cache utilisations due to contiguous memory layout.

# **Mathlike** - Code can more closely resemble standard mathematical notation.

# ## What is an Array?

# An array is a multidimensional table of elements that all have the same type.

# Each dimension (called an axis) has a length, this is the number of elements long it is.

# Arrays have a type of data that each element is a member of (e.g. float, int).

# The lengths of each axis, when taken together, define the shape of the array.

# ![A diagram showing an array](array_diagram.png)

# ## Array Programming with NumPy

# NumPy provides support for array programming in Python.

# It's the fundamental building block for Python's scientific computing stack and is used in many libraries including: Pandas, Matplotlib, Scipy, and PyTorch.

# In addition to basic array programming, it also contain an assortments of fast operations such as Fourier transforms, linear algebra, and basic statistcs.

# NumPy is built on top of two more fundamental technologies: Basic Linear Algebra Subprograms (BLAS) and Linear Algebra Package (LAPACK).

# # Importing NumPy

# In[1]:


import numpy as np


# ## Arrays in NumPy: the ndarray class

# In[2]:


# creation using NumPy's array constructor
np.array([1, 2, 3])


# In[3]:


# we can create a two-dimensional array by passing in a list of lists
arr = np.array([[0.1, 3.3], [1.1, 5.2]])
arr


# In[4]:


# arrays have some properties that are useful to know about
print("arr.ndim =", arr.ndim)
print("arr.shape =", arr.shape)
print("arr.size =", arr.size)
print("arr.dtype =", arr.dtype)
print("arr.itemsize =", arr.itemsize)
print("arr.data =", arr.data)


# In[5]:


# the data type is infered from the argument but can also be specified explicitly
arr = np.array([1, 2, 3], dtype=np.int16)
arr


# # Understanding shapes

# The shape property of an array is normally straight-forward to understand. It's a tuple where the length of each axis is shown at that axis's index.

# e.g. (64, 3, 256, 256) means there are 4 axes with:
# 
# Axis 0 has 64 elements, 
# 
# Axis 1 has 3 elements, 
# 
# Axis 2 has 256 elements, 
# 
# Axis 3 has 256 elements.

# However, if an array only has one axis then its shape is written like so $(n,)$, where $n$ is the length of the axis, which in this case is the number of elements.

# Note - this notation is used because the shape is a tuple and the way that tuples with one element are written in Python is as $(element,)$ in order to make the notion different from an expression in brackets. 

# However, you might want to be more explicit about row and column vectors by having an explicit extra dimension. For example: 

# In[6]:


# let's have a look
row = np.array([1,2,3])
explicit_row = np.array([[1,2,3]])
explicit_col = np.array([[4],[5],[6]])

print("row: ", row.shape)
print("explicit_row: ", explicit_row.shape)
print("explicit_col: ", explicit_col.shape)


# # Other ways to create arrays
# NumPy provides various ways to create arrays in addition to the array constructor. These functions commonly take a tuple specifying the size and an optional dtype.

# In[7]:


# create an array full of zeros
np.zeros((2, 2))


# In[8]:


# create an array full of ones
np.ones((2, 2))


# In[9]:


# create an array full of a specified value
np.full((3,3), 55)


# In[10]:


# create an array but don't initalise its memory
# content is based on the current content of the allocation memory
# faster than initalising but only use if you are overwriting afterwards
np.empty((2, 2))


# In[11]:


# create an array of values between a start and a stop values with a specified number of steps
np.linspace(0, 99, num=10)


# In[12]:


# create an array of values between a start and a stop values with a specified size of step
np.arange(0, 99, 5)


# # Basic Array Operations

# Now that we know how to create arrays, let's look at some basic operations for transforming their elements.

# In[13]:


# let's declare a couple of arrays to manipulate
a = np.full((2,2), 4)
b = np.full((2,2), 3)
a, b 


# In[14]:


# we can perform many common mathematical operators, for example
print(a+b)
print(a-b)
print(a*b)
print(a/b)


# Note that we are using operators to perform these operations. These also have equivalent implementations as functions in NumPy. Sometimes these are more readable.

# In[15]:


# we can perform many common mathematical operators, for example
print(np.add(a,b))
print(np.subtract(a,b))
print(np.multiply(a,b))
print(np.divide(a,b))


# Notice that these are all operating on the elements of the arrays individually. Not all array operators are like this. For example:

# In[16]:


# matrix multiplication
a @ b


# In[17]:


np.dot(a, b)


# # Broadcasting

# So far we have looked at operations where the arrays are the same shape. However, NumPy supports performing operations on arrays of different shape, with some limitations. The term broadcasting is used to describe how Numpy treats these arrays during such operators.

# The most basic example would be operators between arrays and scalars. Let's say we wanted to multiply every element in an array by three.

# In[18]:


# we could create an array of the same shape full of threes.
a = np.full((2,2), 4)
b = np.full((2,2), 3)
a * b


# In[19]:


# but there is a simpler notation
a * 3


# What's going on here? We can think of the scalar 3 being replicated for every element in a. It's as though it's being stretched out.

# ![A diagram showing an array](broadcasting_diagram.png)

# # Accessing and modifying elements

# In[20]:


# like lists and strings, we can use the subscript operators to 
# retrive a single element of an array
arr[0]


# In[21]:


# we can also use it to modify the value
arr[0] = 9
arr


# In[22]:


# arrays can have multiple dimensions, so we need a syntax for indexing them
# for this we use a comma to seperate the indices for each dimension
arr = np.array([[1,2,3],[4,5,6]])

# not that the indices start at axis 0 (rows) and go up by 1 each time, so columns is next.
arr[1,2]

# thinking about rows and columns only really makes sense for 2d arrays


# In[23]:


# as with other indices, negative numbers start from the end and count back
arr[-1,-1]


# # Slices and Indexing

# In[24]:


# Like lists and string, we can use slices to retrive parts of arrays
# remember the slice syntax is start:stop:step
# NumPy extends this idea to work in N dimensions. For example:
arr[0:1,1:2]


# In[25]:


# we can also index with an integer array
# the array just specifies the position in the array
arr = np.array([10,20,30,40,50,60])
indices = np.array([3,4,5])
arr[indices]


# In[26]:


# when the array being indexed is multidimensional then the index refers to the first axis
arr = np.array([[1,2,3],[4,5,6],[7,8,9]])
indices = np.array([1,1,2])
arr[indices]


# In[27]:


# indexing with a boolean array is a powerful way of selecting elements
# we call this a boolean mask
arr = np.array([[1,2,3],[4,5,6]])
mask = np.array([[True, False, True],[False, False, True]])
arr[mask]


# In[28]:


# Using boolean operators to selected elements
arr = np.array([[1,2,3],[4,5,6]])
mask = arr < 3
print(mask)
arr[mask]


# In[29]:


# we can write this more consisely by putting the boolean expression in line with the indexing operation
arr[arr < 3]


# # Basic Aggregation Operations

# In[30]:


arr = np.array([[1,2,3],[4,5,6]])
print(np.mean(arr))
print(np.std(arr))
print(np.min(arr))
print(np.max(arr))


# # Finding Unique Values
# Sometimes it's useful to find all the unique values in a dataset. For example, we might have a table of data with labels specifying some category and want to find all the categories.

# In[31]:


arr = np.array([1,2,1,2,3,4])
np.unique(arr)


# # Transpose
# Getting the transpose of an array is useful in many circumstances. For example, if we wanted to convert a row vector into a column vector.

# In[32]:


row = np.array([[1,2,3]])
print(row)
print(row.shape)
print(row.T.shape)


# In[33]:


# we can do this with matrices
arr = np.array([[1,2,3],[4,5,6],[7,8,9]])
arr, arr.T


# # Reshaping
# Sometimes we might want to reshape an array, so it has a different number of axes and/or a different number of elements per axis.
# 
# This can be done using the reshape function.

# In[34]:


arr = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
reshaped = np.reshape(arr, (4,3)) 
print(arr)
print(arr.shape)
print(reshaped)
print(reshaped.shape)


# # Loading and Saving arrays

# There are several ways to load and save NumPy arrays to disk.

# There is a binary format for NumPy that uses the extension .npy.

# It uses the `np.save` and `np.load` functions.

# The `np.genfromtext` function lets us save NumPy arrays to Comma Seperated Value (csv) files.

# The `np.savetxt` function lets us load NumPy arrays from csv files.

# In[35]:


# for example, let's load a csv of house prices
house_prices = np.genfromtxt("data/houseprices.csv", delimiter=',', skip_header=1)
house_prices[:5,:]


# In[36]:


# then save it back out under a different name
np.savetxt("data/houseprices2.csv", house_prices, delimiter=",")


# # Summary

# - Why array programming is useful for data processing. 

# - How to import NumPy and create arrays.

# - Basic Array Operations and Broadcasting

# - Indexing, Slicing, and Masking with Boolean Operators

# - Aggregating, Transposing, and Reshaping

# - Loading and Saving

# ## Exercise
# In the exercise, please read in the file `data/grades.csv`, compute the mean and standard deviation of the grade column, then write the these values out to a file as an array. 
