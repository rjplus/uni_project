#!/usr/bin/env python
# coding: utf-8

# # Classes
# 
# Programming in Python
# 
# School of Computer Science, University of St Andrews

# ## Motivation
# How can we model a length?

# In[1]:


# Easy: use an int or a float
x = 17


# How about a point in 2D space?

# In[2]:


# tuple (x, y)
point = (17, 12)


# Now how about a circle plotted in 2D space?

# In[3]:


# tuple (x, y, radius)
circle = (17, 12, 5)


# What if the circle has a colour?

# In[4]:


# tuple (x, y, radius, r, g, b)
circle = (17, 12, 5, 0, 128, 255)


# We can write code that uses this

# In[5]:


print(f"Circle at ({circle[0]}, {circle[1]}) with radius {circle[2]}")


# Now what if we want to introduce a $z$ coordinate?
# - Have to update existing code
# - Starting to struggle to keep all these variables straight
# - Errors likely!
# - Complex objects might want something more sophisticated

# ## Classes
# * Good way to structure code
# * Less code replication
# * Constrain functionality
# * May be easier to debug
# * If you have any experience with Java, you may already know that classes are great!

# ## Python has classes!
# * Python is object-oriented (*if you want it to be*)
# * https://docs.python.org/3/tutorial/classes.html
# * Python package = collection of modules
# * Python module can be a collection of classes
# * But (*remember if coming from Java*) **everything is public**

# ### Syntax
# ```python
# class ClassName:
#     <statement-1> # normally, a function definition
#     ...           # but other statements are allowed 
#     <statement-N> # and sometimes useful
# ```
# * indent the content of the class
# * `CamelCase` names for classes and `lower_case_with_underscores` for functions and methods

# # Example: a simple class for greetings

# In[6]:


class Greetings:
    """This class implements greetings"""

    def hello_world(self):
        """A traditional greeting from a new programming language.
        See https://en.wikipedia.org/wiki/%22Hello,_World!%22_program
        """
        # the meaning of the argument `self` to be explained below
        return "Hello, world!"
    
    def ukrainian_salute(self):
        """See https://en.wikipedia.org/wiki/Slava_Ukraini"""
        return "Слава Україні!"   


# **Class instantiation**

# In[7]:


h = Greetings()


# In[8]:


print(h.hello_world()) # calling a method from this class


# In[9]:


print(h.ukrainian_salute())


# In[10]:


h # an instance of the class `Greetings`


# In[11]:


type(h)


# In[12]:


help(Greetings) # displays a list of methods defined in this class


# ## The meaning of self
# * The first argument of a method refers to the object itself
# * By convention, it's usually called `self`
# * But code which does not follow it may be less readable to others
# * And it is plausible that some tools to browse classes may rely on it
# * Methods may call other methods by using method attributes of the `self` argument

# ## But what if there is no self?

# In[13]:


class HelloWorldNoSelf:
    """A class to demonstrate a method without `self` argument"""

    def hello():
        return "Hello, World!"


# In[14]:


h = HelloWorldNoSelf()


# In[15]:


h.hello()


# ### Equality of objects

# In[16]:


class HelloWorld:
    """A simple class"""
    
    def hello(self):
        return "Hello, World!"


# In[17]:


a = HelloWorld()


# In[18]:


b = HelloWorld()


# In[19]:


a == b


# In[20]:


type(a)


# # Storing data in a class

# In[21]:


import time
class DeepThought:
    """There is an answer. But, I'll have to think about it."""
    delay_seconds = 10
    def answer(self):
        # wait for the specified number of seconds
        time.sleep(self.delay_seconds) # uses `self`
        return 42


# In[22]:


a = DeepThought()
a.answer()


# In[23]:


a.delay_seconds


# In[24]:


a.question = "The Ultimate Question Of Life, the Universe and Everything"


# In[25]:


a.question


# ## Initialisation

# In[26]:


class Circle:
    def __init__(self, x, y, radius, red, green, blue):
        self.x = x
        self.y = y
        self.radius = radius
        self.red = red
        self.green = green
        self.blue = blue
        
    def area(self):
        return 3.1415 * self.radius * self.radius
    
    def color(self):
        return (self.red, self.green, self.blue)


# In[27]:


c = Circle(17, 12, 5, 0, 128, 255)


# In[28]:


c.radius


# In[29]:


c.green


# In[30]:


c.area()


# In[31]:


c.color()


# In[32]:


# still can store some more data
c.counter = 1


# In[33]:


while c.counter < 10:
    c.counter = c.counter * 2


# In[34]:


c.counter


# In[35]:


# can also delete data
del(c.counter)


# In[36]:


c.counter # now gives an error


# ## Exercise
# 
# Write a class that represents students on this course.  It should capture:
# - Name
# - Date of birth
# - Modules codes taken
# 
# and should have a method that prints the student's details in a readable fashion.
# 
# Then initialise an instance that represents you!

# In[37]:


class Student:
    def __init__(self, name, date_of_birth, modules):
        self.name = name
        self.date_of_birth = date_of_birth
        self.modules = modules
        
    def print_details(self):
        print(
            self.name,
            "was born on",
            self.date_of_birth, 
            "and is taking",
            ", ".join(self.modules[:-1]),
            "and",
            self.modules[-1],
        )

michael = Student("Michael Young", "19/04/1991", ["CS5901", "CS5902", "CS5905", "CS5999"])
michael.print_details()

