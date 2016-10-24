# -*- coding: utf-8 -*-
"""
Created on Mon Oct 24 15:53:50 2016

@author: perumal
"""
def memoize(f):
    memo = {}
    def helper(x):
        if x not in memo:
            memo[x] = f(x)  ## Here the function f(x) is actually fib(x)
        return memo[x]
    return helper
    
    
def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)   ### Here also the redefined function is called (memoize(fib))
    
fib = memoize(fib)  ## decorate function which calls the helper function

print(fib(40))


"""
powerful function to avoid calculating the function multiple times. 
In case, of fibonacci series, it does not perform the calculation of fib(n-1) or fib(n-2) everytime 

For example, when doing webscraping, if the website url is already checked, 
we can completely avoid scraping the website and continue with the next web url
"""
