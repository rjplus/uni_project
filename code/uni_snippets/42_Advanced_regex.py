#!/usr/bin/env python
# coding: utf-8

# # Advanced regular expressions
# 
# Programming in Python
# 
# School of Computer Science, University of St Andrews

# ## Previously
# - Simple find-and-replace
# - Search using regex: `re.search` and `re.match`
# - Replace using regex: `re.sub`
# - Repetition: `*` and `+`
# - Special characters: `.` `\b` `\d` `\s` `\w` and complements

# ## Today
# - Character classes
# - Specified-length repetition
# - Capturing groups

# In[1]:


import re


# ## A tricky problem

# In[2]:


text = "Launch prices for the Nintendo 64 were $199 in the US, £250 in the UK and ¥25,000 in Japan"


# In[3]:


re.findall("([^\\d\\s])([\\d,]+)\\b", text)


# How did we get to the string above?

# ## Groups
# - Part of a match pattern can have an option in it
# - We use `(x|y)` syntax

# In[4]:


text = "If you are happy, then we are happy and we are likely to remain happy"
re.search("(we|you|they) are", text)


# ## Capturing groups
# - Aside from allowing options, groups have another purpose
# - They mark a part of the search pattern that should be *captured* and treated separately

# In[5]:


match = re.search("(we|you|they) are", text)  # matches
print(match.group(0))  # whole match
print(match.group(1))  # first captured group


# In[6]:


text = "I think Amelia is tall, Oliver is short and Grace is medium-height."
match = re.search("\\b(\\w+) is (\\w+)\\b", text)
print(match.group(0))
print("Noun:", match.group(1))
print("Adjective:", match.group(2))


# Find multiple matches with `re.finditer`

# In[7]:


for match in re.finditer("\\b(\\w+) is (\\w+)\\b", text):
    print("Noun:", match.group(1))
    print("Adjective:", match.group(2))
    print()


# **Note:** `re.findall` uses captured groups if available, and ignores the rest of the string

# In[8]:


re.findall("\\b(\\w+) is (\\w+)\\b", text)


# In[9]:


re.findall("(\\b(\\w+) is (\\w+)\\b)", text)


# ## Character classes
# - We've seen some special character classes: `\d` `\s` `\w`
# - We've also seen their complements: `\D` `\S` `\W`
# - But we can define our own classes using the characters `[]^`

# In[10]:


code = "PsfLsXsqNxZsNBs0sp8xYJ3ssSfsoRsH1xas9Ps"
re.findall("..s", code)


# In[11]:


re.findall("(x|N|J|9).s", code)


# `[...]` matches any character inside the brackets

# In[12]:


re.findall("[xNJ9].s", code)


# `[^...]` matches any character *not* inside the brackets

# In[13]:


re.findall("[^xNJ9].s", code)


# In[14]:


text = "aardvark abacus Adam Adrian bag Bartholomew bale"
words = re.findall("\\w+", text)
print(words)


# In[15]:


names = re.findall("[A-Z]\\w*", text)  # [A-Z] matches any character in the range
print(names)


# ## Repeating a specified number of times
# - `x*`: 0 or more times
# - `x+`: 1 or more times
# - `x?`: 0 or 1 times
# - `x{n}`: n times exactly

# In[16]:


code = "PsfLsXsqNxZsNBs0sp8xYJ3ssSfsoRsH1xas9Ps"
re.search("s{2}", code)


# In[17]:


re.search("[A-Z]{2}", code)


# ## Back to the N64 price example

# In[18]:


text = "Launch prices for the Nintendo 64 were $199 in the US, £250 in the UK and ¥25,000 in Japan"
# get list of tuples of the form (currency, value)


# ## Regex can get complex!
# See some examples at <https://www.variables.sh/complex-regular-expression-examples/>:
# - URL: `(https?:\/\/)?([\da-z\.-]+)\.([a-z\.]{2,6})([\/\w \.-]*)*\/?`
# - Decimal number: `[+-]?([0-9]*[.])?[0-9]+`
# - Time (AM/PM): `(0?[1-9]|1[0-2]):[0-5]\d\s?(am|pm)?`

# ## Exercise
# Write a function that takes a string and returns a boolean indicating whether it is a valid email address or not
# 
# The full email address spec is rather complicated, so just use the restrictions specified at <https://help.xmatters.com/ondemand/trial/valid_email_format.htm>
# 
# Next modify your function so that instead of returning a boolean it returns the email's *domain*, or `None` if the address is invalid
