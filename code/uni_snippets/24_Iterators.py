#!/usr/bin/env python
# coding: utf-8

# # Iterators
# 
# Programming in Python
# 
# School of Computer Science, University of St Andrews

# ## Iteration, iteration, iteration!
# * We will first consider examples of iterating over objects of various types:
#     * iterations over list
#     * iterations over text
#     * iterations over lines
#     * iterations over set
#     * iterations here and there!
#     * iterations everwhere!!!
#     
# *(inspired by Dr. Seuss)*

# ### Iterating over a list

# In[1]:


for i in [1, 2, 3, 4]:
    print(i)


# In[2]:


for i in [1, 2, 3, 4]:
    # `end` is the string appended after the last printed value (newline by default)
    print(i, end=' ')


# ### Iterating over a set

# In[3]:


for i in set([4, 2, 3, 1]):
    print(i)


# ### Iterating over a range

# In[4]:


for i in range(5):
    print(i, end=' ')


# In[5]:


for i in range(2, 17, 3):
    print(i, end=' ')


# ### Iterating over a string

# In[6]:


for i in "Hello":
    print(i,end=' ')


# ### Iterating over a tuple

# In[7]:


for i in (1, 2, 3, 4):
    print(i, end=' ')


# ### Iterating over a dictionary

# In[8]:


d = {'x':3, 'y':1, 't':2}


# In[9]:


# over unsorted keys
for key in d:
    print(key, end=' ')


# In[10]:


# over sorted keys
for k in sorted(d.keys()):
    print(k, end=' ')


# In[11]:


# over sorted values
for v in sorted(d.values()):
    print(v, end=' ')


# In[12]:


# over dictionary items
for t in d.items():
    print(type(t), t)


# In[13]:


d.items()


# In[14]:


type(d.items())


# ### Iterating over a text file

# In[15]:


linenr=1
for line in open("27_Iterators.ipynb"):
    print(line, end='')
    linenr = linenr + 1
    if linenr>12:
        break


# ### Iterating over `enumerate`

# In[16]:


names = ['Alice', 'Bob', 'Clara', 'Doctor']


# In[17]:


enumerate(names) # will iterate over (index,value) pairs


# In[18]:


for i in enumerate(names):
    print(i)


# ### Iterating over `zip`

# In[19]:


names = ['Alice', 'Bob', 'Clara', 'Doctor']


# In[20]:


othernames = ['in Wonderland', 'the Builder', 'Oswald', 'Who']


# In[21]:


for n1, n2 in zip(names, othernames):
    print(n1,n2)


# ## How does this work?
# * The object to iterate over is called the *container* object
# * `for` calls `iter()` on the *container* object
# * `iter` returns an *iterator* object
# * the latter must have a method `__next__` to access elements of the container one at a time
# * the `__next__` method is called via the function `next()`
# * when there are no more elements, `__next__` raises a `StopIteration` exception, which terminates the loop
# * the iterator object also must support a method `__iter__` to allow the use of `for` and `in` with both containers and iterators
# * see the low level demonstration of this process below

# In[22]:


s = 'abc'


# In[23]:


it = iter(s)


# In[24]:


it


# In[25]:


next(it)


# In[26]:


next(it)


# In[27]:


next(it)


# In[28]:


next(it)


# ## Example: Iterating backwards

# In[29]:


class Reverse:
    """Iterator for looping over a sequence backwards."""
    
    def __init__(self, data):
        self.data = data
        self.index = len(data)
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index - 1
        return self.data[self.index]


# In[30]:


for i in Reverse([1, 2, 3, 4]):
    print(i,end=' ')


# In[31]:


for i in Reverse('abcdefghijklmnopqrstuvwxyz'):
    print(i,end='')


# In[32]:


for i in Reverse('never odd or even'):
    print(i,end='')


# ## Exercise
# * Let $A$ and $B$ be two sets. Their Cartesian product $C = A \times B$ is the set of all ordered pairs $(x, y)$ such that $x$ belongs to $A$ and $y$ belongs to $B$
# * Develop the code to support iterating over $A \times B$
# * A hypothetical Python session may look like this
# ```
# >>> for t in IteratorCartesian([1,2,3],['a','b']):
# ...     print(t)
# ... 
# (1, 'a')
# (2, 'a')
# (3, 'a')
# (1, 'b')
# (2, 'b')
# (3, 'b')
# ```
