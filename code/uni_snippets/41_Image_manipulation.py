#!/usr/bin/env python
# coding: utf-8

# # Image manipulation in Python
# 
# Programming in Python
# 
# School of Computer Science, University of St Andrews

# ## Basics of image manipulation
# - How the images may be stored in NumPy arrays?
# - What else do you need to know to use [scikit-image](https://scikit-image.org/)?
# 
# This episode is based on the introduction to the Data Carpentry lesson ["Image processing with Python"](https://datacarpentry.org/image-processing/), which we suggest for further reading

# ## Which libraries do we need?

# In[1]:


import numpy as np
import matplotlib.pyplot as plt
# a library to read and write a wide range of image data
import imageio.v3 as iio 
# to enable interactive matplotlib features
get_ipython().run_line_magic('matplotlib', 'widget')


# ## Working with pixels

# In[2]:


eight = iio.imread(uri="data/eight.tif")
plt.imshow(eight)


# ## How is it stored?
# - it's an array of arrays
# - more specifically, NumPy arrays
# - it's a 5x3 matrix of 15 pixels

# In[3]:


print(eight)
print(type(eight))
print(type(eight[0]))
print(eight.shape)


# ## We can edit specific pixels

# In[4]:


zero = iio.imread(uri="data/eight.tif")
zero[2,1]= 1.0
# Next line creates a new figure for `imshow` to display the output.
# Otherwise, plt.imshow() would overwrite the image in the cell above
fig, ax = plt.subplots()
plt.imshow(zero)
print(zero)


# ## More colours
# - Before, we used only two colours
# - Can have more if we use other numbers (or fractions)
# - Use numbers from 0 to 255 to have 256 different colours
#   (or 256 different levels of grey)
# - Why such colours: default colour map (`cmap`) used by this library

# In[5]:


three_colours = iio.imread(uri="data/eight.tif")
three_colours = three_colours * 128
three_colours[2,:] = 255.
fig, ax = plt.subplots()
plt.imshow(three_colours)
print(three_colours)


# ## Same data in grayscale
# - 0: black
# - 255: white
# - 128: medium grey

# In[6]:


fig, ax = plt.subplots()
plt.imshow(three_colours,cmap=plt.cm.gray)


# ## Even more colours
# - Would be impractical to have a one-to-one mapping between numbers and millions of colours
# - Instead, the solution is to store more numbers in more dimensions

# In[7]:


# set the random seed so we all get the same matrix
pseudorandomizer = np.random.RandomState(5901)
# create a 5 × 5 grid of random colours
checkerboard = pseudorandomizer.randint(0, 255, size=(5, 5, 3))
checkerboard


# In[8]:


# restore the default map as you show the image
fig, ax = plt.subplots()
plt.imshow(checkerboard)


# ## Why the blue square is blue?

# In[9]:


blue_square = checkerboard[1, 0, :]
blue_square


# ## Channels
# - Colours mapped to dimensions of the matrix are referred to as channels
# - We can extract channels by multiplying the image array representation by a list that has 1 for the channel we want to keep and 0s for the rest

# In[10]:


red_channel = checkerboard * [1, 0, 0]
fig, ax = plt.subplots()
plt.imshow(red_channel)


# In[11]:


green_channel = checkerboard * [0, 1, 0]
fig, ax = plt.subplots()
plt.imshow(green_channel)


# In[12]:


blue_channel = checkerboard * [0, 0, 1]
fig, ax = plt.subplots()
plt.imshow(blue_channel)


# ## Display the format-specific metadata

# In[13]:


metadata = iio.immeta(uri="data/eight.tif")
metadata


# ## Finally...
# - Digital images are represented as rectangular arrays of square pixels
# - They use so called `left-hand` coordinate system:
#   - the origin in the upper left corner
#   - the x-axis going right
#   - the y-axis going down
#   - like counting down rows and counting columns from left to right
# - scikit-image stores images as multi-dimensional NumPy arrays
# - scikit-image images specify channels in the RGB order
