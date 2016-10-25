# -*- coding: utf-8 -*-
"""
Created on Tue Oct 25 10:43:34 2016

@author: perumal
"""

import shelve
d = shelve.open("test.shelve")
for key in d:
    print(key, ' contains ', d[key])
    
d.close()