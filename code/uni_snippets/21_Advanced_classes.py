#!/usr/bin/env python
# coding: utf-8

# # Advanced classes
# 
# Programming in Python
# 
# School of Computer Science, University of St Andrews

# ## More on initialisation

# In[1]:


class Hello:

    """A class to show __init__ method"""

    def __init__(self, name):
        self.name = name

    def hello(self):
        """A function to show using `self` to refer to a data attribute"""
        return "Hello from " + self.name


# In[2]:


t = Hello("Clara")


# In[3]:


t.hello()


# In[4]:


help(Hello) # see `__init__` entry below


# # Example class with info, __init__, __str__ and __repr__

# In[5]:


class MyClass:
    """A list wrapper class to demonstrate __init__, __str__ and __repr__ methods"""
    def __init__(self, info):
        "Store an underlying list as a data attribute while creating an instance of the class"
        self.info = info
    def size(self): 
        return len(self.info)
    def __str__(self): # overwrite "print"
        return "<" + str(self.info) + ">"
    def __repr__(self): # if we want to generate a valid Python input
        return "MyClass(" + str(self.info) +")"


# In[6]:


a = MyClass([1, 4, 5]) # instance object


# In[7]:


print(a)


# In[8]:


a


# In[9]:


a.size


# In[10]:


a.size()


# In[11]:


a.info # data attribute


# In[12]:


a.info.append(4)


# In[13]:


print(a)


# In[14]:


a.__module__ # a "knows" a lot about itself. Use `dir` to find out!


# In[15]:


dir(a)


# In[16]:


help(MyClass)


# ### Warning
# * data attributes override method attributes with the same name!

# In[17]:


a.size = 1


# In[18]:


a.size() # now gives an error


# ## Another pitfall

# In[19]:


class Dog:
    """The Dog Who Wouldn't Be (a tribute to Farley Mowat)"""

    tricks = []

    def __init__(self, name):
        self.name = name

    def add_trick(self, trick):
        self.tricks.append(trick)


# In[20]:


f = Dog("Floppy")
p = Dog("Ping")


# In[21]:


f.add_trick("stores everything")
p.add_trick("barks loudly")


# In[22]:


p.tricks # unexpected sharing


# * Class variables shared by all instances
# * Instead, one should use an instance variable

# In[23]:


class Dog:
    """Another Dog Who Wouldn't Be"""

    def __init__(self, name):
        self.name = name
        self.tricks = []    # creates a new empty list for each dog

    def add_trick(self, trick):
        self.tricks.append(trick)


# In[24]:


f = Dog("Floppy")
p = Dog("Ping")
f.add_trick("stores everything")
p.add_trick("barks loudly")


# In[25]:


f.tricks


# In[26]:


p.tricks


# ## Methods can call other methods

# In[27]:


class Bag:

    def __init__(self):
        self.data = []
    
    def add(self, x):
        self.data.append(x)
    
    def addtwice(self, x):
        self.add(x)
        self.add(x)


# In[28]:


a = Bag()


# In[29]:


a.data


# In[30]:


a.add(2)


# In[31]:


a.data


# In[32]:


a.addtwice(1)


# In[33]:


a.data


# # Using `pass`
# * Create an empty employee record

# In[34]:


class Employee:
    pass


# In[35]:


john = Employee()


# In[36]:


john.name = 'John Smith'; john.dept = 'computer lab'; john.salary = 30000


# In[37]:


john


# In[38]:


john.name


# # Inheritance

# In[39]:


class Scientist:

    def __init__(self, name, occupation):
        self.name = name
        self.occupation = occupation

    def scientist_name(self):
        return self.name
    
    def scientist_occupation(self):
        return self.occupation

    def __str__(self): # overwrite "print"
        return "%s is a %s" % (self.name, self.occupation)


# In[40]:


alice = Scientist("Alice", "biochemist")


# In[41]:


alice


# In[42]:


print(alice)


# In[43]:


help(alice)


# In[44]:


alice.scientist_name()


# In[45]:


alice.scientist_occupation()


# In[46]:


class Algebraist(Scientist):
    """All algebraists are mathematicians (?) and may be able to program"""
    def __init__(self, name, can_code):
        Scientist.__init__(self, name, "mathematician")
        self.is_coder = can_code

    def can_code(self):
        return self.is_coder
    
    def __str__(self):
        if self.is_coder is True:
            return "%s is a %s who can write programs" % (self.name, self.occupation)
        else:
            return "%s is a %s who can not write programs" % (self.name, self.occupation)


# In[47]:


bob = Algebraist("Bob", False)


# In[48]:


bob.scientist_name()


# In[49]:


clara = Algebraist("Clara", True)


# In[50]:


print(bob)


# In[51]:


print(clara)


# In[52]:


bob.can_code()


# In[53]:


help(bob) # this shows how methods are resolved and inherited


# In[54]:


if (isinstance(alice, Scientist)):
    print("Alice is a scientist")


# In[55]:


if (isinstance(bob, Scientist)):
    print("Bob is a scientist")


# In[56]:


if not (isinstance(alice, Algebraist)):
    print("Alice is not an algebraist")


# In[57]:


if (isinstance(bob, Algebraist)):
    print("Bob is an algebraist")


# In[58]:


if (isinstance(clara, Algebraist)):
    print("Clara is an algebraist")


# * Multiple inheritance: https://docs.python.org/3.9/tutorial/classes.html#multiple-inheritance

# ## Exercise
# Go back to your solution to the exercise in the first Classes lecture.
# - Add code so that the student is displayed nicely when passed to `print`
# - Add a subclass `OnlineStudent` which also contains information on where the student lives
# - Test your code!

# ## Solution

# In[59]:


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
        
    def __str__(self):
        return f"<{self.name}: student studying {len(self.modules)} modules>"


class OnlineStudent(Student):
    def __init__(self, name, date_of_birth, modules, location):
        Student.__init__(self, name, date_of_birth, modules)
        self.location = location


michael = OnlineStudent("Michael Young", "19/04/1991", ["CS5901", "CS5902", "CS5905", "CS5999"], "Mexico")
print(michael)
print(michael.location)

