# -*- coding: utf-8 -*-
"""
Created on Tue Oct 25 10:52:46 2016

@author: perumal
"""

import pickle

f = open("my_data.pkl", "br")  ### open my pickled_data for binary read operation
a = pickle.load(f)
print(a)