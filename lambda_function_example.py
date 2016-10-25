# -*- coding: utf-8 -*-
"""
Created on Tue Oct 25 12:14:12 2016

@author: perumal
"""

### Lambda functions are functions without names or throwaway functions, which are not used any more
#### it can more than one parameters, but the same amount of parameters mut be given when calling

g = lambda x:x+1   ### lambda function does not have name, it does not have loops inside

g1 = lambda x, y: x + 1
#g1(3) ### gives an error
g1(3,5) ### gives output 4
##
c = [12.3, 11.2, 9.9, 10.3, 12.8, 9.8, 8.1]
print(list(map(lambda x: 1.8*x + 32 if x < 10 else 8, c)))  ###can use a condition inside a lambda function

"""
Similar to
def f(x):
    return x + 1
"""

from math import sin

def f(func, x):
    return func(x)
    
print(f(sin, 3))
print(f(lambda x: x+7, 3))




c = [12.3, 11.2, 9.9, 10.3, 12.8, 9.8, 8.1]  # temperature values


""""
def celsius2fahrenheit(t):
    return 9/5*t + 32
    
F = []
for t in c:
    F.append(celsius2fahrenheit(t))
print(F)
This whole process can be done with a simple lambda function
"""
def mapping(func, values):
    res = []
    for el in values:
        res.append(func(el))
    return res
        
#print(mapping(celsius2fahrenheit, c))

print(mapping(lambda x: 9/5*x +32, c))


"""
MAP  function
"""
print(list(map(lambda x: 9/5*x + 32, c)))  ####MAP  Reduces the above mapping function and
                                           #### lambda function in a single line




"""
map on multiple lists using lambda function
"""
a = [1, 2, 3, 4]
b = [17, 12, 11, 10]
c = ['a', 'b', 'c', 'd']
print(list(map(lambda x,y: x+y, a, b)))

print(list(map(lambda x,y, z: (x+y)*z, a, b, c)))
