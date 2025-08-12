#!/usr/bin/env python
# coding: utf-8

# # Pandas
# 
# Programming in Python
# 
# School of Computer Science, University of St Andrews

# # What is Pandas?

# Pandas is a library for data manipulation.

# Useful for reading, exploring, transforming, and writing table-like data with columns of different data-types.

# This is what makes it distinct from NumPy, the heterogeneous nature of the data.

# It’s similar to a spreadsheet but can do many of the selection and transformation operations you might do with a database.

# # Importing Pandas
# Much like NumPy there is a convention when importing Pandas.

# In[1]:


import pandas as pd


# # Series

# A Series is one-dimensional ndarray with labels for each of its elements – called its index.

# An index can be any hashable value, such as a string or an integer. They default to 0, 1, 2, 3, …

# A Series can also have name (optionally).

# We can declare a Series like so, passing in a value for each element:

# In[2]:


pd.Series(['a', 'b', 'c', 'c'])


# This will add a Range Index by default, that is one that starts a 0 and goes up in increments of 1.

# Let's say that we want to use a set of the string of our own invention as the indices. We can do this by passing a list to the `index` keyword argument.

# In[3]:


s = pd.Series(['a', 'b', 'c', 'c'], 
        index=['row0', 'row1', 'row2', 'row3'])
s


# ## Indexing Series
# If we want to select a value from a series, there are two methods: 

# - `loc` – retrieves that value with that label in the index

# In[4]:


s.loc['row2']


# - `iloc` – retrieves the value at that location

# In[5]:


s.iloc[2]


# Watch out! The subscript operator uses `loc`. This can be a source of bugs.

# ## Data Frames

# - A Data Frame is two-dimensional data structure, used to represent table-like data consisting of cells, organised into rows and columns.

# - Each column in a Data Frame is a Series. 

# - You can think of a Data Frame as a dictionary of Series.

# - All Series in the Data Frame have identical indices.

# - Think of the indices as defining the row names and the keys for each Series as defining the column names.

# - They are declared using the `DataFrame` constructor. For example:

# In[6]:


pink_floyd = pd.DataFrame({
    "name": ["Nick", "Richard", "Dave"],
    "instrument": ["drums", "keyboards", "guitar"],
    "age": [77, 65, 74]
})
pink_floyd


# You can declare an empty Data Frame with the column names using the `columns` keyword argument.

# Data Frames actually have a property called `columns`. Note - it is of type index but it's actually the column names, not the rows.

# In[7]:


band = pd.DataFrame(columns=['name', 'instrument', 'age'])
band


# In[8]:


band.columns


# It can be useful to get a quick look at the start of any data. To do this we can use the `head` method to select as many rows at the start as we want.

# In[9]:


pink_floyd.head(2)


# ## Indexing Data Frames

# Indexing pandas dataframes has the same label and position options as the pandas Series.

# In[10]:


pink_floyd.loc[[0, 2], ['name', 'age']]


# We can also use a boolean condition (a *predicate*) to select specific rows.

# In[11]:


predicate = pink_floyd['age'] > 71
over_71 = pink_floyd[predicate]
over_71


# We can transform Data Frames in lots of ways. For example, let's say we wanted to add another column to the frame. We can do this by assigning to the column, like so:

# In[12]:


hometown = ['London', 'Great Bookham', 'Cambridge']
pink_floyd['hometown'] = hometown
pink_floyd


# Note that we can assign to a column with a single value and it will fill the column.

# In[13]:


pink_floyd['can_sing'] = True  
pink_floyd


# ## Reading and Writing CSV files using Pandas
# Pandas can also be used to read and write CSV files using the `pd.read_csv` and `pd.to_csv` functions.

# In[14]:


grades = pd.read_csv('data/grades.csv')
grades.head()


# Let's add a column and save it back out.

# In[15]:


grades['Normalised Grade'] = grades['Grade'] / 100
grades.head()


# In[16]:


grades.to_csv('data/normed_grades.csv', index=False)


# ## Getting Summary Statistics
# Like in other similar libraries, it's possible to get summary statistics about your data using Pandas. For example:

# In[17]:


# what is the mean grade
grades['Grade'].mean()


# In[18]:


# what is the median attendence
grades['Attendance'].median()


# You can generate a standard set of statistics about specfic columns using the `describe` function.

# In[19]:


grades[['Grade', 'Attendance']].describe()


# ## Summary

# - Series

# - DataFrames

# - Indexing and Manipulating DataFrames

# - Loading and Saving DataFrames

# - Using describe to generate summary statistics of the data frame.

# ## Exercise
# 
# Read in the data in `data/us-states.csv` and print out:
# - The quartiles of the state populations;
# - The state codes, separated by commas, in the order that the states joined the union;
# - The GDP per capita of each state (GDP divided by population)
