# -*- coding: utf-8 -*-
"""Assignment 6

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1vJV604pdstG6VkJDLEH70oc0BBivJOtz

Question 1:
"""

onehole=['A','D','O','P','Q','R']
def hole(val,a):
  if a in onehole:
    return val+1;
  elif a =='B':
    return val+2;
  else:
    return val;
str1=input("Enter string in upper case :").upper();
print("string in upper case is : ", str1)
count=0;
for i in str1:
  count=hole(count,i);
print("Count of holes is : ", count)

"""MAP():

syntax: map(function,iterable)
"""

def sqr(a):
  return a*a
result=map(sqr,[1,2,3,4,5])
print(list(result))

def dif(a,b):
  return a-b
print(list(map(dif,[1,2,3,4,5],[5,4,3,2,1])))

"""# Lambda():
They don't have name.
syntax: lambda argument: expression
"""

x = lambda a: a*a*a
x(4)

def owal(a):
  if a in ['a','e','i','o','u']:
    return lambda val: val+1;
  else:
    return lambda val: val;
count=0
z=owal('o')
print(z)
print(z(count))