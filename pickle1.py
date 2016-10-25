# -*- coding: utf-8 -*-
"""
Created on Tue Oct 25 09:17:44 2016

@author: perumal
"""

import pickle

d = {'a':3, 'b':5, 'c':10, 'bla':897, 'xyz':2, 'm':99}
lst = [4,5,6]
fh = open('my_data.pkl', 'bw')  ### filename_fh = open('name_of_the_file.with_any_extension , 'bw'=binary write)
pickle.dump((d, lst),fh)  ## pickle(any_object_you_want_to_pickle, multiple objects can be a tuple, file_fh)
fh.close()

### does not save the variable name

