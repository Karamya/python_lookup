# -*- coding: utf-8 -*-
"""
Created on Tue Oct 25 14:29:30 2016

@author: perumal
"""

p = [('Peter', 114, 42, 3467.87),
     ('Eve', 129, 37, 3100.03),
     ('Bill', 105, 42, 7239.34),
     ('Stella', 125, 36, 3983.45),
     ('Eve', 117, 37, 3490.99),
     ('Peter', 99, 48, 6780.21),
     ('Bill', 105, 41, 6780.21)]
    
print(sorted(p))

print(sorted(p, key = lambda x: (x[1]+x[2], x[3]*x[1], x[0], x[1], x[2]))) 
"""
here we map every tuple to a new tuple (x1+x2, x3+x1, x0, x1, x2)
it sorts the list as if the list is a new tuple

"""
print(sorted(p, key = lambda x:x[2]))
"""
Here it creates the sorting with the element of the index at 2
"""
lst = [31, 409, 4, 41, 53, 5, 500, 9, 91]

print(sorted(lst))

print(sorted(lst, key = str))  ### it will make the elements of the list to string and sort it

print(sorted(lst, key = lambda x:str(x)[::-1])) 



"""
Beware - see below
"""
print(lst.sort(key=lambda x:str(x)[::-1]))
"""
 Here the original list is rewritten and saved
"""

print(sorted("Python is great!"))


lst = [31, 409, 4, 41, 53, 5, 500, 9, 91]
lst = lst.append(33)
print(lst)   ### should not be done, as it returns a None if it changes an existing object
             ### and returns the same reference

s = 'This is Great'
s2 = s.upper()
print(s2)    ### returns the ouput 'THIS IS GREAT', as strings are immutable,
            ### so, it creates a new object and is assigned to a new reference s2





lst = [(3, 5), (1, 9), (1,3), (1, 9), (1, 4), (4, 3), (4, 9), (9, 3), (10, 1), (10, 4)]
print(sorted(lst))
print(sorted(lst, key = lambda x: (x[0], -x[1])))  ### with -x[1], it is decreasing order for x[1]
print(sorted(lst, key = lambda x: (x[0], -x[1]), reverse = True))  ### Look what x[1] does
print(sorted(lst, key = lambda x: (x[0], x[1]), reverse = True)) 
