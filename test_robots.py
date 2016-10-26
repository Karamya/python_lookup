# -*- coding: utf-8 -*-
"""
Created on Wed Oct 26 14:22:05 2016

@author: perumal
"""

from robots import Robot, Robot1  # imports Robot class from robots.py

x = Robot("Oscar")

Robot.say_hi(x)
x.say_hi()
#print(Robot.__dict__)
#print(x.get_name())
#print(x.__dict__)    #### outputs "{'_Robot__name': 'Marvin'}"  
#                     #### whatever starts with an underscore _Robot... are modified and cannot be modified
#
y = Robot('Henry')

y.set_name(x.get_name())

y.name = x.name

print(x.name)         #### prints "Marvin"

x.name = "Oscar"


m = Robot1("Adam")

m.say_hi()

n = Robot1("Eve", "Atlas")

y = eval(repr(m))

z = m + n

print(z)