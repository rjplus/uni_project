#!/usr/bin/env python
# coding: utf-8

# # Matplotlib
# Programming in Python
#   
# School of Computer Science, University of St Andrews

# - Matplotlib is a plotting library for Python.

# - It can be used to create static, animated, and interactive data visualisation

# - There are two ways to use Matplotlib
#     - The Object Oriented (OO) API
#     - The PyPlot API (works like plotting in Matlab)

# ## Basic Concepts

# - **Figures** represent the thing that you are going to draw the plot onto. This might be a window, a file, some memory, or a Jupyter notebook.

# - **Axes** represent a region on the figure that defines a coordinate system so that points can be plotted onto it. For example, these can be x-y coodinates.

# - **Axis** are number line like objects. An axes has one for each of its dimensions.

# - **Artists** is the name given to anything that draws something onto a figure or axes. For exmaple: text, lines, and rectangles.

# ## Basic Usage
# First let's look at the basics of how to use the Matplotlib using the OO API.

# In[1]:


import matplotlib.pyplot as plt


# In[2]:


fig, ax = plt.subplots()


# Let's create a basic plot and look at some of its parts. The axes object that we created has a method called plot that lets us plot points on it.

# It takes in a numpy array specifying the x coordinates, then one specifying the y coordinates. It also takes in an optional label keyword argument that is used if we add a legend.

# To create different kinds of plots, there are different methods on the axes. For example: plot, bar, and scatter.

# In[3]:


import matplotlib.pyplot as plt

# import numpy so we can create the arrays
import numpy as np

# use the arange function to create two arrays
# with values starting a 0, ending at 2, and
# increasing by 0.02 each time
x = np.arange(0, 2, 0.02)
y = np.arange(0, 2, 0.02)

# create the figure and the axes for the figure
fig, ax = plt.subplots()

# plot the data onto the axes
ax.plot(x, y, label='linear')


# Let's make the figure a bit more readable by adding a title, labels to the axis, and a legend.

# In[4]:


import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0, 2, 0.02) 
y = np.arange(0, 2, 0.02)

fig, ax = plt.subplots()
ax.plot(x, y, label='linear')

# add labels to the x and y axis
# for this we used the axes object
ax.set_xlabel('x label')
ax.set_ylabel('y label')

# set the title of the figure
ax.set_title('A Plot')

# add a legend
ax.legend()


# What if we want to show more than one thing on the plot.

# In[5]:


import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0, 2, 0.02)
y = np.arange(0, 2, 0.02)

fig, ax = plt.subplots()

ax.plot(x, y, label='linear')
ax.plot(x, y**2, label='quadratic')
ax.plot(x, y**3, label='cubic')

# add labels to the x and y axis
# for this we used the axes object
ax.set_xlabel('x label')
ax.set_ylabel('y label')

# set the title of the figure
ax.set_title('A Plot')

# add a legend
ax.legend()


# ## Summary

# - The concepts of figures, axis, axes, and artists.

# - Basic importing and plotting.

# - How to add more detailed information and layout to the plot.

# - For more information check out the official documentation here: <https://matplotlib.org/stable/tutorials/index>

# # Exercise
# For this exercise, load the file 'population.csv' and create a plot of the population of each country over the years 1900 to 2000.
