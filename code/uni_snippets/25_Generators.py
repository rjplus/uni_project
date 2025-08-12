#!/usr/bin/env python
# coding: utf-8

# # Generators
# 
# Programming in Python
# 
# School of Computer Science, University of St Andrews

# ## Generators
# * Iterators are *classes* that produce a sequence of values
# * Generators are *functions* that produce a sequence of values
# * It can be expensive to generate an entire list at once (e.g. using list comprehensions)
# * Generator does so called "lazy generation", yielding one element at a time

# ## A simple generator function
# * Note the `yield` statement, which makes it special

# In[1]:


def count_from(n): 
    while True:
        yield n 
        n += 1


# In[2]:


for i in count_from(1):
    if i < 11:
        print(i, end=' ')
    else:
        break


# ## A generator function returns a generator object

# In[3]:


count_from(-5)


# In[4]:


for i in count_from(-5):
    if i < 6:
        print(i, end=' ')
    else:
        break


# ## How does it work?
# * generator function is only run when you use it as an iterator
# * first time function is run, runs until `yield`
# * `yield` acts like `return` but allows to continue another execution cycle
# * each subsequent call runs the execution cycle one more time
# * this goes on and on, until `yield` no longer returns

# In[5]:


def count_from_info(n):
    while True:
       print("--- before yield, n =", n)
       yield n
       n += 1
       print("--- after yield, n =", n)


# In[6]:


for i in count_from_info(1):
    print('*** new iteration')
    if i <= 3: 
        print('*** i =', i)  
    else:
        break


# ## Generator comprehension vs list comprehension

# In[7]:


squares = [n*n for n in range(0,11)]
squares


# Generator comprehension uses same notation as list comprehension but with round brackets

# In[8]:


squares = (n*n for n in count_from(1))


# Instead of returning a list, generator comprehension returned another generator!

# In[9]:


squares


# In[10]:


for j in squares:
    if j <= 1000:
        print(j, end=' ')
    else:
        break


# ## It can even be used with `enumerate`

# In[11]:


enum = enumerate(squares)


# In[12]:


for x in enum:
    print(x, end=' ')
    if x[0] > 10:
        break


# - But why does it start from 1089?
# - Need to reset `squares` to fix this

# In[13]:


squares = (n*n for n in count_from(1))
enum = enumerate(squares)


# In[14]:


for x in enum:
    print(x, end=' ')
    if x[0] > 10:
        break


# # Generating prime numbers

# In[15]:


# a helper function to check if `n` is a multiple of some number from the list `numbers`
def is_multiple(numbers, n):
    for i in numbers:
        if n % i == 0:
            return True # n is a multiple of i
    return False


# In[16]:


def prime_generator():
    primes = []
    for i in count_from(2):
        if not is_multiple(primes, i):
            primes.append(i)
            yield i


# In[17]:


for i in prime_generator():
    if i >= 500:
        break
    print(i, end=" ")


# ## Exercise
# * Rewrite the code of `prime_generator` above to avoid using `count_from`
# * Test it on the same example to generate all primes less than 500
# 

# In[18]:


def prime_generator2():
    primes = []
    i = 1
    while True:
        i += 1
        if not is_multiple(primes, i):
            primes.append(i)
            yield i


# In[19]:


for i in prime_generator2():
    if i >= 500:
        break
    print(i, end=" ")

