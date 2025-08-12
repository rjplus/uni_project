#!/usr/bin/env python
# coding: utf-8

# # Style & PEP 8
# 
# Programming in Python
# 
# School of Computer Science, University of St Andrews

# ## Style
# - Correct code will run correctly
# - But horrible code will be difficult to maintain
# - We want *good style*

# ## General tips
# 
# - Some style tips are relevant for all languages
# - Let's see some examples

# Use meaningful names

# In[1]:


x = 78000


# Use lots of small functions instead of deep nesting

# In[2]:


for classroom in school:
    if classroom.capacity > 10:
        for student in classroom:
            if student.age >= 21 and len(student.criminal_convictions) == 0 and student.has_driving_licence:
                print(student.name, "should be considered")
    else:
        print("No bus needed for", classroom.name)


# Use comments effectively

# In[3]:


# add 10 to size_of_building
size_of_building += 10


# In[4]:


# make sure year is 2024
year = 2026


# # PEP 8
# * Style Guide for Python Code: http://python.org/dev/peps/pep-0008/
# * Widely used, and worth following most of the time

# 4-space indentation (no tabs)

# In[5]:


for i in range(50):
      print(size(rocket) - i)


# 79 character line width

# In[6]:


print("Please note that", PROGRAM_NAME, "is open-source software under the", PROGRAM_LICENCE, "licence and the source code is available for free.")


# Spaces around operators and after commas, but not directly inside bracketing constructs:

# In[7]:


a=f (1,2) + g ( 3,4 )


# * Blank lines to separate functions and classes
# * Larger blocks of code inside functions
# * Comments on their own line (where possible) 
# * Use docstrings (`"""docstring"""`)
# * `CamelCase` names for classes and `lower_case_with_underscores` for functions and methods
# * UTF-8 encoding

# ## Style is important!
# - Your coworkers will thank you for good style
# - So will your future self
# - So will university lecturers marking your work!

# ## Exercise
# Modify the following code so that it follows the PEP 8 style.

# In[8]:


# Returns a boolean stating whether the given integer is prime!
def is_prime(n):
        if n <= 1:
              return False
        for i in range(2,n):
              if n%i==0:
                      return False
        return True

count=0
num=2

while count<100:
        if is_prime( num ):
            print( num )
            count += 1
        num += 1


# ## Solution

# In[9]:


def is_prime(n):
    """Returns a boolean stating whether the given integer is prime."""
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

count = 0
num = 2

while count < 100:
    if is_prime(num):
        print(num)
        count += 1
    num += 1

