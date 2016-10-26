# -*- coding: utf-8 -*-
"""
Created on Wed Oct 26 10:40:01 2016

@author: perumal



Typical usage:

from contextlib import contextmanager

@contextmanager
def some_generator(<arguments>):
    <setup>
    try:
        yield <value>
    finally:
        <cleanup>
    
"""

from contextlib import contextmanager

@contextmanager    ### decorator
def func():
    print("With statement has started")
    yield #the block after with is executed
    print("With statement ends now")
    
with func():
    print("Whatever has to be done will be done")
    
  
##############################################################################
###                             HTML Tags                                  ###
##############################################################################  

@contextmanager
def tag(name):
    print("<%s>" %name)
    yield
    print("</%s>" %name)

with tag("h1"):
    print("My string")   
    
##############################################################################
###                             HTML Tags                                  ###
##############################################################################  

@contextmanager
def   tag1(name):
    print("<%s>" %name)
    yield
    print("</%s>" %name)

with tag1("body") as r:
    with tag1("p") as s:
        print("Some text!")
        
        
#equivalent to 
#with tag1("body") as r, tag1("p") as s:
#    print("Just some text!")

    
##############################################################################
###                    Best example - File Handling                        ###
##############################################################################   
    
with open("test.shelve.dir", "w") as fh:
    fh.write("as asdd werrrr qrrtt")
    fh. write("as saasada asdadasdad ")

with open("test.shelve.dir") as fh:
    for line in fh:
        print(line)
