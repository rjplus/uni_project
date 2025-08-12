#!/usr/bin/env python
# coding: utf-8

# # Debugging in Python
# 
# Programming in Python
# 
# School of Computer Science, University of St Andrews

# *“Bugs - as such little faults and difficulties are called - show themselves and months of intense watching, study and labour are requisite before commercial success or failure is certainly reached.”*
# 
# Thomas Edison, personal communication, 1878

# Obviously your Python programs should be perfect from start ...
# 
# But here in the real world ...

# * Floating point vs integer division (in Python 2)

# In[1]:


float(4)/3==4/3 # will be False in python2


# * Confusing syntax (`split` vs `join`)

# In[2]:


pangram = "The quick brown fox jumps over the lazy dog"


# In[3]:


words = pangram.split(" ")


# In[4]:


words


# In[5]:


text = words.join(" ")


# In[6]:


text =" ".join(words)


# In[7]:


text


# * 2nd iteration over a file without reopening

# In[8]:


my_file = open("43_Debugging.ipynb")
for line in my_file:
    print(".",end="")
# second loop silently never runs (so you don't even see an error because of undefined `do_something_else`)
for line in my_file:
    print("?",end="")
    do_something_else(line)


# * Typos in variable names (not declared – not revealed) 

# In[9]:


numbers = 0
for i in range(1,6):
    numbrs = numbers + i
print(numbers) # prints 0 instead of 15


# # Debugging in `prinf`-style

# In[10]:


a=3
print("a = %s" % a)
a="hello"
print("a = %s" % a)


# In[11]:


for i in range(5):
    i=i+1
    print("i = %d" % i)


# # Assertions

# In[12]:


a=3
assert a == 3
print("a is %s" % a)
a=4
assert a == 3


# # `code.interact`

# * Python interactive console is great for experimenting
# * `code.interact` allows you to break out into interactive console during execution of a program
# * see https://docs.python.org/3.9/library/code.html?highlight=code.interact#code.interact

# **Example**
# 
# ```
# import code
# 
# a = 3
# 
# def f(x):
#     a=x*x
#     code.interact(local=locals())
#     return a
# ```

# ```
# >>> f(10)
# Python 3.9.1 (v3.9.1:1e5d33e9b9, Dec  7 2020, 12:10:52) 
# [Clang 6.0 (clang-600.0.57)] on darwin
# Type "help", "copyright", "credits" or "license" for more information.
# (InteractiveConsole)
# >>> a
# 100
# >>> x
# 10
# >>> ^D
# 100
# >>> a
# 3
# ```

# # pdb

# Interactive debugger, which enables all the usual debugging functionality:
# * break points
# * stepping through executing flow
# * inspecting the stack
# 
# 
# See https://docs.python.org/3/library/pdb.html?highlight=pdb#module-pdb
# 

# ** Example: `printf.py`**

# `printf.py`
# 
# ```
# #!/usr/bin/env python3
# 
# a=3
# print("a is %s" % a)
# a="hello"
# print("a is %s" % a)
# 
# for i in range(10):
#     i=i+1
#     print("i is %d" % i)
# ```

# **Example 2: `printf_pdb.py`**
# ```
# #!/usr/bin/env python3
# 
# import pdb
# 
# a=3
# print("a is %s" % a)
# a="hello"
# print("a is %s" % a)
# pdb.set_trace()
# 
# for i in range(10):
#     i=i+1
#     print("i is %d" % i)
# ```

# ```
# $ python3 printf_pdb.py
# a is 3
# a is hello
# > <path_to_file>/printf_pdb.py(11)<module>()
# -> for i in range(10):
# (Pdb) print(a)
# hello
# (Pdb) 
# ```

# ## Further information
# * https://wiki.python.org/moin/PythonDebuggingTools
