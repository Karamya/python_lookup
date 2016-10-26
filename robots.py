# -*- coding: utf-8 -*-
"""
Created on Wed Oct 26 14:21:50 2016

@author: perumal
"""

##############################################################################
####              Magic function                                          ####
############################################################################## 

class Robot():
    
    def __init__(self, name):     ### magic function
        self.set_name(name)
        
    def get_name(self):
        return self.__name   #### two underscores before the variable means, it is a private variable
                             #### and cannot be accessed from outside
    
    def set_name(self, name):
        if name == "Oscar":
            self.__name = "Marvin"
        else:
            self.__name = name
    
    def say_hi(self):
        print("Hi, I am " + self.__name)
        
    name = property(get_name, set_name)    ### changing the property
                                           ### the variable name gets first get_name and does set_name
 
##############################################################################
####              Magic function                                          ####
############################################################################## 

class Robot1():
    
    def __init__(self, name, brand = "Kuka"):     ### magic function
        self.name = name
        self.brand = brand
        
    @property
    def name(self):          #### getter
        return self.__name   #### two underscores before the variable means, it is a private variable
                             #### and cannot be accessed from outside
    @name.setter
    def name(self, name):    #### setter
        if name == "Oscar":
            self.__name = "Marvin"
        else:
            self.__name = name
    
    @property
    def brand(self):        #### getter function
        return self.__brand
        
    @brand.setter
    def brand(self, brand):  ### setter functions
        if brand in {"Kuka", "Atlas", "Siemens"}:  ####{} no element by element 
        ###comparison is done, much faster for huge number of elements than in a list
            self.__brand = brand
        else:
            self.__brand = "Kuka"            
            
    def __str__(self):
        return self.name + " made by " + self.brand
        
    def __repr__(self):
        return 'Robot1("' + self.name + '", "'+ self.brand + '")'
        
    def __add__(self, other):
        return Robot1(self.name + "-" + other.name, 
                     self.name + " and " + other.name)
        
    def say_hi(self):
        print("Hi, I am " + self.__name)
        
