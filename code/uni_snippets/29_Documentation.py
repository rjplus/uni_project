#!/usr/bin/env python
# coding: utf-8

# # Documentation
# 
# Programming in Python
# 
# School of Computer Science, University of St Andrews

# ## Document your code
# It's important to make it clear what your code does.  This helps:
# - Maintenance
# - Debugging
# - Usage
# 
# But how do we do it?

# ## Option 1: Self-documenting code
# Write code that is easy to understand
# - Meaningful identifiers
# - Small functions
# - Logical program order

# ```python
# def authenticate_user(database_connection):
#     username = get_username_from_command_line()
#     password = get_password_from_command_line()
#     encrypted = encrypt_password(password, LOCAL_KEY)
#     if is_valid_credentials(
#         database_connection, 
#         username, 
#         encrypted
#     ):
#         return True
#     return False
# ```

# ## Option 2: Comments
# If necessary, add comments
# - Explain the intention of the code
# - Draw attention to surprising behaviour
# - Explain anything that looks odd
# - Don't say anything obvious
# - Don't say anything untrue

# ```python
# def gcd(a, b):  # gcd: Greatest common divisor
#     # Highest number that divides both a and b
#     # Based on the Euclidean algorithm (see textbook)
#     while b != 0:
#         t = b
#         b = a % b  # assumes both a and b are ints
#         a = t
#     return a
# ```

# ## Option 3: Docstrings
# 
# - String surrounded by `"""triple quotes"""`
# - Inserted at start of a function, class or module
# - Explains what the thing does
# - Helps understanding when:
#   - Looking at the code
#   - Looking at generated doc
# - See PEP 257 for conventions
#   - <https://peps.python.org/pep-0257/>

# One-liners:
# ```python
# def kos_root():
#     """Return the path to the KOS root directory."""
#     global _kos_root
#     if _kos_root: return _kos_root
#     ...
# ```

# Multi-line docstrings:
# ```python
# def complex(real=0.0, imag=0.0):
#     """Form a complex number.
# 
#     Keyword arguments:
#     real -- the real part (default 0.0)
#     imag -- the imaginary part (default 0.0)
#     """
#     if imag == 0.0 and real == 0.0:
#         return complex_zero
#     ...
# ```

# Don't include complicated formatting:
# ```python
# def kos_root():
#    """<p class="function">Return the path to the
#    <code>KOS</code> root directory.</p>"""
# ```

# Don't repeat information from the method signature:
# ```python
# def gcd(a, b):
#     """function gcd with args (a, b)
#     
#     Returns the greatest common divisor of a and b.
#     """
# ```

# Include useful information like return types, examples and related functions.

# In[1]:


def pickle(obj):
    """Return a string representation of the object `obj`

    This function takes any object, and uses the `pickle` and `base64` modules
    to create a string which represents it.  This string consists only of
    alphanumeric characters, hyphens and underscores.  The object `obj` can
    later be reconstructed from this string using the `unpickle` function.

    Examples
    --------
    >>> pickle("Hello world")
    'gANYCwAAAEhlbGxvIHdvcmxkcQAu'
    >>> unpickle("gANYCwAAAEhlbGxvIHdvcmxkcQAu")
    'Hello world'

    """
    b = pickle_to_bytes(obj)  # object to bytes
    b64 = urlsafe_b64encode(b)  # bytes to base64 bytes
    s = b64.decode(CHAR_ENCODING)  # base64 bytes to string
    return s


# Document your modules and classes as well!

# In[2]:


"""Objects used for storing and manipulating integer sequences."""

class Calculator
    """A model calculator for sequences of operations.
    
    Attributes
    ----------
    base (int): The base to use for display (e.g. decimal)
    """
    def __init__:
        ...


# ## Help systems use docstrings
# - When you use `help(x)` or `x?` the help displayed is from docstrings
# - You can also generate HTML documentation from your docstrings using `pydoc`
# - Include docstrings in your own code, and others will be able to use these tools!

# In[3]:


def sum_of_squares(a, b):
    """Returns the sum of the squares of the two numbers a and b.
    
    Both parameters should be ints or floats.
    """
    return a ** 2 + b ** 2


# In[4]:


help(sum_of_squares)


# ## Summary
# - Documentation is critical for your code to be understood and maintained
# - If there are no docs, code is unusable!

# ## Exercise
# - Find your solution to the reversing exercise in the Lists lecture
# - Turn it into a function
# - Write a docstring, including expected input types and an example call
# - Use the help system to view the documentation

# ## Solution

# In[5]:


def reversed_string(a):
    """Return a string which is the reverse of the input.
    
    a should be of type str.
    
    Example
    -------
    >>> reversed_string("abacus")
    "sucaba"
    """
    return a[::-1]


# In[6]:


help(reversed_string)

