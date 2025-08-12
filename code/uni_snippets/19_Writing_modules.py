#!/usr/bin/env python
# coding: utf-8

# # Writing modules
# 
# Programming in Python
# 
# School of Computer Science, University of St Andrews

# ### Celsius vs Fahrenheit: some functions

# In[1]:


def c2f(c):
    f = (c * 1.8) + 32
    return f


# In[2]:


c2f(100)


# In[3]:


def f2c(f):
    c = (f - 32) / 1.8
    return c


# In[4]:


f2c(100)


# In[5]:


a=f2c(451) # a tribute to Ray Bradbury
print(a)


# ### How to change output formatting

# In[6]:


print(f't = {a:.3e}') # 3 digits after the point
print(f't = {a:.2f}') # 2 digits after the point 


# ### This is still not good – it is not documented!

# **Solution: docstrings**
# 
# * triple quotation marks
# * `pydoc` to generate text or html
# * may be called `pydoc3` on your machine

# Create the file `c2f.py`:
# 
# ```python
# # Convert between Celsius and Fahrenheit
# 
# """Simple program to demonstrate functions"""
# ```

# Now try:
# ```
# pydoc c2f
# pydoc -w c2f
# open c2f.html
# ```

# Now add some code to  `c2f.py`

# ```python
# # Convert between Celsius and Fahrenheit
# 
# """Simple program to demonstrate functions"""
# 
# def c2f(c):
#     """Convert degrees C to degrees F"""
#     f = (c * 1.8) + 32
#     return f
# 
# def f2c(f):
#     """Convert degrees F to degrees C"""
#     c = (f - 32) / 1.8
#     return c
# ```

# Then try again 
# ```
# pydoc c2f
# pydoc -w c2f
# open c2f.html
# ```

# ## Example: Fibonacci series

# In[7]:


def fib(n):
    """Write the first n entries in the Fibonacci series"""
    a, b = 0, 1
    while b < n:
        print(b)
        a, b = b, a+b


# In[8]:


fib(100)


# In[9]:


def fib2(n):
    """Return the first n entries in the Fibonacci series"""
    result = []
    a, b = 0, 1
    while b < n:
        result.append(b)
        a, b = b, a+b
    return result


# In[10]:


fib2(100)


# ## This works everywhere

# In[11]:


help(fib)


# In[12]:


help(fib2)


# ## This is specific for Jupyter notebooks

# In[13]:


get_ipython().run_line_magic('pinfo', 'fib')


# In[14]:


get_ipython().run_line_magic('pinfo', 'fib2')


# # Modules

# * Separate files with variable/function definitions
# * Can be used via `import` and `from`
# 

# Copy the functions we defined to a file `fibo.py`

# ```python
# def fibonacci(n):
#     """write Fibonacci series up to n"""
#     a, b = 0, 1
#     while b < n:
#         print(b)
#         a, b = b, a+b
#         
# def fibonacci2(n):
#     """return Fibonacci series up to n"""
#     result = []
#     a, b = 0, 1
#     while b < n:
#         result.append(b)
#         a, b = b, a+b
#     return result
# ```

# In[15]:


import fibo


# In[16]:


fibo.fibonacci(10)


# In[17]:


fibo.fibonacci2(10)


# ### Alternatively, use explicit import by specifying function name

# In[18]:


from fibo import fibonacci, fibonacci2


# In[19]:


fibonacci2(500)


# ## Reloading a module
# ```python
# import importlib
# importlib.reload(fibo)
# ```

# # How to code:
# 
# * Use the interpreter interactively in the terminal or via Jupyter
# * Use a text editor to write plain text programs
# * Combine both of the above
# * Use JupyterLab: https://jupyterlab.readthedocs.io/
# * Use an IDE: see some at https://wiki.python.org/moin/IntegratedDevelopmentEnvironments

# ## Exercise
# * Create a file `imperial_to_metric.py` with functions to convert from yards to metres, and from acres to hectares
# * Include docstrings that make it clear what your functions do
# * In the cell below, import your module and try calling the functions.
# * Get Jupyter to print out the help message 
