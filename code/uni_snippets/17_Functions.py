#!/usr/bin/env python
# coding: utf-8

# # Functions
# 
# CS5901: Programming in Python
# 
# School of Computer Science, University of St Andrews

# We are now getting comfortable writing code.  We started with some simple conversions:

# In[1]:


temp_f = 70
temp_c = ((temp_f - 32) * (5/9))
print(temp_c)


# We even know about different types now, so we might do some safety checks:

# In[2]:


temp_f = 70
if type(temp_f) is not int:
    temp_c = "Not a number"
else:
    temp_c = ((temp_f - 32) * (5/9))
print(temp_c)


# We might even want to make our model more advanced:

# In[3]:


temp_f = 70
if type(temp_f) is not int:
    temp_c = "Not a number"
elif temp_f < -459.67:
    temp_c = "Too cold!"
else:
    temp_c = ((temp_f - 32) * (5/9))
print(temp_c)


# Now what if we want to use our code several times?

# In[4]:


temp_f = 70
if type(temp_f) is not int:
    temp_c = "Not a number"
elif temp_f < -459.67:
    temp_c = "Too cold!"
else:
    temp_c = ((temp_f - 32) * (5/9))
print(temp_c)

temp_f = 105
if type(temp_f) is not int:
    temp_c = "Not a number"
elif temp_f < -459.67:
    temp_c = "Too cold!"
else:
    temp_c = ((temp_f - 32) * (5/9))
print(temp_c)

temp_f = -2000
if type(temp_f) is not int:
    temp_c = "Not a number"
elif temp_f < -459.67:
    temp_c = "Too cold!"
else:
    temp_c = ((temp_f - 32) * (5/9))
print(temp_c)


# Our code could get a lot more complicated
# 
# - Use a patient's height, weight, age, heart rate and temperature to recommend a medication
# - Find all the prime numbers up to $n$
# - Search through a DNA sequence looking for all occurrences of a given pattern
# 
# Could be hundreds of lines
# 
# Let's not copy and paste!

# ## Functions
# - A way of re-using a block of code
# - Has a name
# - Can have inputs
# - Can have outputs

# ## Writing a function
# - Create a `def` block
# - Declare your parameters
# - Write the code
# - Return a value (optional)

# In[5]:


def fahr_to_cent(temp_f):
    if type(temp_f) is not int:
        return "Not a number"
    elif temp_f < -459.67:
        return "Too cold!"
    else:
        return ((temp_f - 32) * (5/9))


# In[6]:


fahr_to_cent(70)


# In[7]:


fahr_to_cent(105)


# In[8]:


fahr_to_cent(-2000)


# ## Advantages
# - We only have to write complicated code *once*
# - If a bug is found, we only have to fix it *once*
# - "Black box model": forget about how a function *works*, just think about what it *returns*
# - Cleaner, simpler code

# ## Arguments
# 
# A function might have just one argument:

# In[9]:


def double(x):
    return 2 * x


# In[10]:


double(12)


# A function might have multiple arguments:

# In[11]:


def print_several_times(n, message):
    for i in range(n):
        print(message)


# In[12]:


print_several_times(5, "hello mum!")


# A function might even have no arguments at all:

# In[13]:


def info_about_me():
    return "My name is Michael and I'm " + str(8 * 4) + " years old."


# In[14]:


info_about_me()


# ## Chaining functions
# 
# We can also *chain* function calls together, using the output of one function as the input of another:

# In[15]:


double(double(5))


# In[16]:


print_several_times(double(3), info_about_me())


# ![chaining-functions.drawio.svg](attachment:chaining-functions.drawio.svg)

# ## Return vs print
# - Can call `print` inside a function
#   - Prints something to screen, then forgets it
# - Can use `return` instead
#   - Value is returned to whoever called the function
#   - Value can be used in any way we want

# In[17]:


def area_of_circle(radius):
    print(3.14 * radius * radius)


# In[18]:


area_of_circle(5.0)


# In[19]:


print(area_of_circle(5.0))


# In[20]:


volume_of_cylinder = 7.5 * area_of_circle(5.0)


# In[21]:


def area_of_circle(radius):
    return 3.14 * radius * radius


# In[22]:


print(area_of_circle(5.0))


# In[23]:


volume_of_cylinder = 7.5 * area_of_circle(5.0)
print(volume_of_cylinder)


# - We nearly always want to use `return` in functions
#   - More flexible
# - Only use `print` in functions if you really mean it
#   - e.g. functions with `print` in the name

# ## Optional arguments
# - Can specify the *default value* of an argument
# - Can then call the function with or without the argument
# - Great for allowing a user to customise functionality

# In[24]:


def introduction(name, town="St Andrews"):
    return "My name is " + name + " and I'm from " + town


# In[25]:


print(introduction("Stefano", "Milan"))
print(introduction("Parvati", "Mumbai"))
print(introduction("Michael"))
print(introduction("Mariana", "Rio de Janeiro"))


# ## Functions are great
# - Makes code easier to understand and maintain
# - A key part of *abstract thinking*
# - Use them liberally!

# ## Exercise
# 
# Here is some code that I want to be able to run.  Define the functions `is_odd_number`, `square` and `meters_to_feet` that it works as intended.  Think about what these should do, based on their names and the way they're being used.

# In[26]:


# your code here

for i in range(10):
    if is_odd_number(i):
        print(square(i))
    else:
        print(meters_to_feet(i))


# ## Solution

# In[27]:


def is_odd_number(n):
    return n % 2 == 1

def square(x):
    return x * x

def meters_to_feet(x):
    return 3.28 * x

for i in range(10):
    if is_odd_number(i):
        print(square(i))
    else:
        print(meters_to_feet(i))

