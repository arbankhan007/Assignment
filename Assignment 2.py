#!/usr/bin/env python
# coding: utf-8
# Write a Python Program to implement your own myreduce() function which works exactly like
Python's built-in function reduce()
# In[ ]:


def my_reduce(func,l):
    first=l[0]
    for i in l[1:]:
        first=func(first,i)
    return first
def func(a,b):
    return a+b
l=[1,2,3,4]

print(my_reduce(func,l))


# Write a Python program to implement your own myfilter() function which works exactly like
# Python's built-in function filter()

# In[69]:


def my_filter(fun,l1):
    l2=[]
    for i in l1:
        if fun(i) !=None:
            l2.append(fun(i))
    return l2
def fun(n):
    if n<10:
        return n
l1=[1,2,10,230,40,36,9,50]
print(my_filter(fun,l1))


# Implement List comprehensions to produce the following lists.
# Write List comprehensions to produce the following Lists
# ['A', 'C', 'A', 'D', 'G', 'I', ’L’, ‘ D’]

# In[30]:


s='ACADGILD'
l=[i for i in s]
l


# 2. ['x', 'xx', 'xxx', 'xxxx', 'y', 'yy', 'yyy', 'yyyy', 'z', 'zz', 'zzz', 'zzzz']

# In[32]:


st='xyz'
l2=[i*n for i in st for n in range(1,4)]
print(l2)


# ['x', 'y', 'z', 'xx', 'yy', 'zz', 'xx', 'yy', 'zz', 'xxxx', 'yyyy', 'zzzz']

# In[40]:


s='xyz'
l3=[i*x*y for x in range(1,3) for y in range(1,3) for i in s]
print(l3)


# [[2], [3], [4], [3], [4], [5], [4], [5], [6]]

# In[41]:


l=[2,3,4,3,4,5,4,5,6]
l1=[[i] for i in l]
l1


# [[2, 3, 4, 5], [3, 4, 5, 6], [4, 5, 6, 7], [5, 6, 7, 8]]

# In[49]:


l=[2,3,4,5]
l=[[i+j for i in l] for j in range(4) ]
l


# [(1, 1), (2, 1), (3, 1), (1, 2), (2, 2), (3, 2), (1, 3), (2, 3), (3, 3)]

# In[51]:


l=[(i,j) for j in range(1,4) for i in range(1,4)]
l


# Implement a function longestWord() that takes a list of words and returns the longest one.

# In[68]:


def longestWord(l):
    n=l
    lword=len(n[0])
    first=n[0]
    for i in l:
        if lword<len(i):
            first=i
            lword=len(i)
    return first

l=['my','name','is','arban','khan']
print('the longest word is',longestWord(l))


# Task 2:

# Write a Python Program(with class concepts) to find the area of the triangle using the below
# formula.
# area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
# Function to take the length of the sides of triangle from user should be defined in the parent
# class and function to calculate the area should be defined in subclass.

# Write a Python function which takes a character (i.e. a string of length 1) and returns True if it is
# a vowel, False otherwise

# In[2]:


def fvowel(n):
    s=n.lower()
    for s in 'aeiou':
        return True
    else:
        return False
print(fvowel('a'))    


# Write a function filter_long_words() that takes a list of words and an integer n and returns the list
# of words that are longer than n.

# In[6]:


def filter_long_words(li,n):
    l=[]
    l1=li
    for i in l1:
        if len(i)>n:
            l.append(i)
    return l
li=['arban','khan','is','a','student']
print(filter_long_words(li,4))
    


# In[ ]:




