#!/usr/bin/env python
# coding: utf-8

# # Unit tests in Python
# 
# Programming in Python
# 
# School of Computer Science, University of St Andrews

# ## unittest - unit testing framework
# - similar to major unit testing frameworks in other languages
# - supports organisation and automation of tests
# - executing them in an independent environment
# 
# Concepts:
# - **test fixture**: actions to prepare to one or more tests, and associated cleanup actions
# - **test case:**: an individual *unit of testing*
# - **test suite**: a collection of test cases and/or test suites
# - **test runner**: a component to run tests and report their results
# 
# See https://docs.python.org/3/library/unittest.html

# ## A small example of using unit tests

# In[1]:


import sys
import unittest
import random


# In[2]:


# a class with two perfect tests which always pass :)
class MyTest(unittest.TestCase):
    def test_one(self):
       # some test code goes here
       pass
    def test_two(self):
       # some test code goes here
       pass


# In[3]:


# test suite
def suite():
    loader = unittest.TestLoader()
    testsuite = loader.loadTestsFromTestCase(MyTest)
    return testsuite


# In[4]:


# test runner: a function to run the tests
def test():
    testsuite = suite()
    runner = unittest.TextTestRunner(sys.stdout, verbosity=2)
    result = runner.run(testsuite)


# In[5]:


# now call the function to run the tests
test()


# ## A more sensible example of using unit tests

# In[6]:


# an example to test some functionality for sequences
class TestSequenceFunctions(unittest.TestCase):

    def setUp(self):
        self.seq = [i for i in range(10)]

    def test_shuffle(self):
        # make sure the shuffled sequence does not lose any elements
        random.shuffle(self.seq)
        self.seq.sort()
        self.assertEqual(self.seq, [i for i in range(10)])

        # should raise an exception for an immutable sequence
        self.assertRaises(TypeError, random.shuffle, (1,2,3))

    def test_choice(self):
        # random choice should return an element from the original sequence
        element = random.choice(self.seq)
        self.assertTrue(element in self.seq)

    def test_sample(self):
        # can not choose 20 distinct random elements out of 10
        with self.assertRaises(ValueError):
            random.sample(self.seq, 20)
        # but it should be possible to pick 5
        for element in random.sample(self.seq, 5):
            self.assertTrue(element in self.seq)


# ## Shorter way to run a test
# 
# (compare with the previous example)

# In[7]:


suite = unittest.TestLoader().loadTestsFromTestCase(TestSequenceFunctions)
unittest.TextTestRunner(verbosity=2).run(suite)


# ## Exercise
# 
# * Convert the code of the last example into an executable Python script that can be run from the command line
