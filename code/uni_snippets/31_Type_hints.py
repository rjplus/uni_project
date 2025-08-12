#!/usr/bin/env python
# coding: utf-8

# # Type hints
# 
# Programming in Python
# 
# School of Computer Science, University of St Andrews

# ## Types in Python
# Recall that Python is *dynamically typed*:
# * you don't have to say what type a variable is when you declare it
# * variables can change type when you assign them
# * no checking is done
# * however...

# ## Type hinting
# - You can add *hints* to your code to specify some types
# - See this example from the official docs:

# In[1]:


def greeting(name):
    return 'Hello ' + name


# In[2]:


def greeting(name: str) -> str:
    return 'Hello ' + name


# <https://docs.python.org/3/library/typing.html>

# Type hints don't **do** anything:

# In[3]:


greeting("Michael")


# In[4]:


greeting(42)


# ## So why use them?

# - External tools can do some checking for you
#   - MyPy type checker
#   - Common IDEs
# 
# - Problems can be detected and flagged to you

# See this example in the PyCharm IDE:
# ![pycharm_type_error.webp](attachment:pycharm_type_error.webp)
# (From <https://realpython.com/python-type-checking/>)

# ## Should I use them?
# Pros
# - Can avoid errors earlier
# - A neat way of documenting expected types
# 
# Cons
# - More cluttered code
# - Loses some benefits of dynamically typed languages

# Alternatives:
# - Make intended types clear in documentation
# - Use obvious "natural" types
# - Use another language!

# ## Exercise
# Read the following code, and add type annotations to the header to hint at the types that it should accept.

# In[5]:


def word_repeated(word, n, use_comma_separator):
    output = ""
    for i in range(n):
        output += word
        if i < n - 1 and use_comma_separator:
            output += ", "
    return output


# In[6]:


word_repeated("hello", 5, False)


# In[7]:


word_repeated("world", 3, True)


# ## Solution

# In[8]:


def word_repeated(word: str, n: int, use_comma_separator: bool) -> str:
    output = ""
    for i in range(n):
        output += word
        if i < n - 1 and use_comma_separator:
            output += ", "
    return output

