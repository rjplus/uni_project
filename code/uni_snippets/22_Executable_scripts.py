#!/usr/bin/env python
# coding: utf-8

# # Executable Python scripts
# 
# Programming in Python
# 
# School of Computer Science, University of St Andrews

# ## First executable program in Python
# - Our aim is to be able to run Python code from a command line
# - Should be as easy as using Unix shell commands like `ls` and `cd`
# - To start with, create a file `hello.py` with the following lines:
# 
# ```python
# # A simple program
# 
# print("Hello, world!")
# ```

# Now we can use a Python interpreter to execute the code
# 
# ```
# $ python hello.py 
# Hello, world!
# $ 
# ```
# However, we still have to call `python`
# 

# ## Transform this into an **executable script**:
# - add one line at the start
# 
# ```bash
# #!/usr/bin/env python
# 
# # A simple program
# 
# print("Hello, world!")
# ```

# - `#!/usr/bin/env python` is there to use the first interpreter found in the `$PATH`.
#   - Could instead use `#!/usr/bin/python` but that would be less flexible.
# - the 2nd line with an empty comment is just a separator
# - need to use `chmod` to set executable permissions, then can run it as follows:

# ```
# $ chmod 755 hello_script.py
# $ ./hello_script.py
# Hello, world!
# $ 
# ```

# 
# # main

# - Next, we revisit an example from the episode on writing modules: `c2f.py`
# - Add a `#!/usr/bin/env python` line at the start
# - Add the following after the conversion functions:
# 
# ```python
# def main():
#     print("100C = ", c2f(100), "F")
#     print("212F = ", f2c(212), "C")
#     
# if __name__ == "__main__":
#     main()
# ```

# See https://docs.python.org/3/library/__main__.html 

# # Program arguments

# Next, put 
# ```python
# import sys
# ```
# in the beginning of the file (just after comments) and replace the last two lines by
# 
# ```python
# if __name__ == "__main__":
#     print("script name is", sys.argv[0])
#     if (len(sys.argv) == 2): # check number of arguments
#         print(sys.argv[1], "C = ", c2f(int(sys.argv[1])), "F")  
# ```   

# Now you are able to do the following:
# ```
# $ ./c2f_main_arg.py 0
# script name is ./c2f_main_arg.py
# 0 C =  32.0 F
# $ ./c2f_main_arg.py 100
# script name is ./c2f_main_arg.py
# 100 C =  212.0 F
# ```

# * See also [Python main() functions](http://www.artima.com/weblogs/viewpost.jsp?thread=4829) by Guido van Rossum

# ## Exercise
# Modify the `fibo.py` file that we showed in the *Writing modules* lecture to turn it into an executable script.
# 
# When run as a script, the file should take an integer as a command-line argument, and print out all the Fibonacci numbers up to that integer.

# You will need to add:
# - a `#!` line at the start;
# - an import for the `sys` package;
# - an `if __name__ == "__main__"` statement at the end.

# ## Solution
# The file should look like the following:

# In[1]:


#!/usr/bin/env python

import sys

def fibonacci(n):
    """write Fibonacci series up to n"""
    a, b = 0, 1
    while b < n:
        print(b)
        a, b = b, a+b

def fibonacci2(n):
    """return Fibonacci series up to n"""
    result = []
    a, b = 0, 1
    while b < n:
        result.append(b)
        a, b = b, a+b
    return result

if __name__ == "__main__":
    if len(sys.argv) == 2: # check number of arguments
        n = int(sys.argv[1])
        print("The first few Fibonacci numbers are:", fibonacci2(n))
    else:
        print("Incorrect number of arguments specified")
        print("Usage: ./fibo.py n")

