# -*- coding: utf-8 -*-
"""
Created on Wed Oct 26 09:14:24 2016
Handling Exceptions 
@author: perumal
"""
#
#while True:
#    try:
#        x = int(input("Please enter a number: "))
#        break
#    except ValueError as err: ##err gives the system error
#        print("error message: ", err)
#        print("No valid number. Try again!")


##############################################################################

##############################################################################

def f(x):
    try:
        z = 10/x
        return z
    except:
        print('Exception in f: Division by Zero')
        raise    ### raises the exception to the place from where this function is called
try:
    y = 0
    f(y)
except:
    print("Exception in main!")
    #raise  #### There is nowhere to catch the raise function, so, the program terminates
           

print("program continues")



##############################################################################
###                  The optional else clause                              ###
##############################################################################
arg = "test.shelve.dir"
try:
    f = open(arg, 'r')
except IOError:
    print('cannot open', arg)
else:  ### useful for cases where the try does not raise an exception
       ### anything before the else is checked, so we can be sure that
       ### the error happens only in the try block
       ### there is a possibility of raising error in else statements
    print(arg, 'has', len(f.readlines()), 'lines') 
    f.close()
    
    
    
##############################################################################
###                  Multiple Exceptions                                   ###
##############################################################################   

import sys

try:
    f = open(arg)
    s = f.readline()
    i = int(s.strip())
    
except IOError as err:
    (errno, strerror) = err.args
    print("I/O error ({0}): {1}".format(errno, strerror))

except ValueError:
    print("No Valid integer in line.")

#except (IOError, ValueError):   #### multiple errors can be catched
#    print("An IOError or a ValueError has occurred")

except:
    print("Unexpected error:", sys.exc_info()[0])
    raise
    
    

##############################################################################
###                      Try... Finally                                    ###
##############################################################################   
    

try:
    x = float(input("Your number: "))
    inverse = 1.0/x
except ZeroDivisionError:
    print('sorry')
    raise
else:
    print("The inverse is ", inverse)
finally: ### this is always done, whether the try is executed or exception block is executed or not
         ### Even if the program terminates, the finally block is executed
    print("There may or maynot be an exception")

print("The inverse: ", inverse)
 

##############################################################################
###                              Assert                                    ###
##############################################################################
"""
The assert statement is intended for debugging statements. It can be seen as 
an abbreviated notation for a conditional raise statement. Assert should not 
be used to catch programming erros like x/0, because python traps such 
programming errors itself.
It is only to test for user defined constraints
"""
x = 3
y = 5
assert x>4, "False"
assert y>4, "False"
   
