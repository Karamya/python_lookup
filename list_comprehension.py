# -*- coding: utf-8 -*-
"""
Created on Tue Oct 25 13:51:32 2016

@author: perumal
"""
from functools import reduce
"""
Filter provides an elegant way to filter out those elements which are true if applied to a function
"""

lst = [3, 5, 12, 6, 7, 8, 9, 20]

print(list(filter(lambda x: x> 10, lst)))

print(list(map(lambda x: x> 10, lst)))


"""
Reduce applies a function to the whole list
"""
y = reduce(lambda x, y: x+y, range(1,101))   ### returns sum of all elements in a list
### reduce is not in python3 any more, so have to import from fuctools import reduce
print(y)


####
temp = (36.5, 37, 37.5, 39, 29.8, 27.3, 25.9)

temp_in_fahrenheit = list(map(lambda x:1.8*x + 32, temp))  ### map function and lambda function
print(temp_in_fahrenheit)

#####

s = {1, 2, 4, 5, 6}
s2 = {8, 5, 6, 9, 2}

print(s|s2) #### print set s union set s2

######

"""

Replacing filter and map

"""
temp = (36.5, 37, 37.5, 39, 29.8, 27.3, 25.9)

y = [1.8*t for t in temp]

"""
instead of 
y = list(map(lambda t: 1.8*t+32, temp))
"""

y = [t for t in temp if t>=30]
"""
instead of 
list(filter(lambda t: t>=30, temp ))

"""

[1.8*t+32 for t in temp if t>=30]

"""
instead of
list(map(lambda t: 1.8*t+32, filter(lambda t: t>=30, temp)))

"""



#####
lst = [31, 409, 53, 91]
print([str(x) for x in lst])
print([str(x)[::-1] for x in lst])
print([int(str(x)[::-1]) for x in lst])

######


"""
A list comprehension can consist of an arbitrary number of for/ins . These can be viewed as nested for loops

"""
x = [2, 4, 6, 8]
y = [3, 0, -5, 1]
sum_xy = [x[i]+y[i] for i in range(4)]


first = ["lust", 'merci', 'fanci', 'art', 'power', 'voice']
last = ['less', 'full']

new_list = [f+l for f in first for l in last]  ### multiple for loops
print(y)

