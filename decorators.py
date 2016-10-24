# -*- coding: utf-8 -*-
"""
Created on Mon Oct 24 15:53:50 2016

@author: perumal
"""
from math import sin, cos


def deco(func):
    def helper(x):
        print("Before calling " + func.__name__)
        res = func(x) * 0.5         ### Modify the actual function
        print("After calling " + func.__name__)
        return res
    help.__name__ = func.__name__
    return helper
 
original_sin = sin
original_cos = cos   
   
sin = deco(sin)
print(sin(2), original_sin(2))

cos = deco(cos)
print(cos(2), original_cos(2))

#### The same decorator can be used for different functions

@deco               ### @deco is same as bla = deco(bla)
def bla(x):
    return x * 0.77777
    
print(bla(1))
#bla = deco(bla)

"""

Before calling sin
After calling sin
0.45464871341284085 0.9092974268256817
Before calling cos
After calling cos
-0.2080734182735712 -0.4161468365471424
Before calling bla
After calling bla
0.388885

"""
