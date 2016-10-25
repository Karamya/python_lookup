# -*- coding: utf-8 -*-
"""
Created on Tue Oct 25 09:24:27 2016

@author: perumal
"""

import shelve  ## think like a book shelf
### Think about dynamically saving in a database
print(__name__)
d = shelve.open("test.shelve")  
""" create test.shelve file for opening and saving
we always use variable d for dictionary. Shelves can have only keys as strings
it is a dictionary, but in lots of cases, this can be used like a database, but not a database 
which can be used by multiple users
"""
d["a"] = [23, 98, 'strings possible', [34, 'Hello']]
d["b"] = {1: 'One', 2: 'Two', 3:'Three'}
if __name__ == "__main__":
    for el in d:
        print(el, d[el])
    

    
    