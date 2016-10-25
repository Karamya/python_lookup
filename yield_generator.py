# -*- coding: utf-8 -*-
"""
Created on Tue Oct 25 16:31:02 2016

@author: perumal
"""

"""
it is possible to write functions that may be resumed after they send a value back
These functions are called generators, because they generate a sequence of values over time
"""

def abc():
    yield('a')
    yield('b')
    yield('c')
    
x = abc()
g = abc()

print(next(x))
print(next(x))
print(next(x))
#print(next(x))
#print(next(x))
#print(next(x))
#print(next(x))
#print(next(x))
#print(next(x))
#print(next(x))


def bcd():
    while True:
        for char in 'abcdefg':
            yield(char)
y = bcd()
print(next(y))
print(next(y))
print(next(y))
print(next(y))
print(next(y))
print(next(y))
print(next(y))
print(next(y))
print(next(y))
print(next(y))
print(next(y))
print(next(y))
print(next(y))
print(next(y))
print(next(y))
print(next(y))
print(next(y))
print(next(y))
print(next(y))
print(next(y))
print(next(y))
print(next(y))
print(next(y))
print(next(y))
print(next(y))


"""
lst = [3,5,6]
for el in lst:
    print(el)
    
    
#####   A for loop works like this using the iter function
x = iter(lst)
print(next(x))
print(next(x))
print(next(x))
"""

"""
########
## PI with generators
The following sequence converges to pi/4 where pi/4 = 1 - 1/3 + 1/5 - 1/7 + .....
########
"""
def pi_series():
    sum = 0
    i = 1.0
    j = 1
    while True:
        sum = sum + j/i
        yield 4*sum
        i = i + 2
        j = j*-1
    



def firstn(g, n):
    for i in range(n):
        yield next(g)
print(list(firstn(pi_series(), 8)))

#####


def ghi():
    s = 'abcdef'
    count = 0
    while True:
        i = (yield s[count % 6])  ### If you send 0 here, then i becomes None. Be careful here as the modulus returns None
        if i: ### Here if it is 0, this is not executed and goes to the else statement
            count = i
        else:
            count += 1
if __name__ == "__main__":
    x = ghi()
    print(next(x))
    print(next(x))
    print(x.send(0)) 
  
###  function x is called and sends integer 4, which is basically after 
###  the yield execution from the previous step 
###  to the yield function which is then assigned to i in the above function 
 
    print(next(x))
    print(next(x))



##### Another example

def efg():
    yield 'a'
    yield 'b'
    yield 'c'
    yield 'd'
    yield 'e'

def firstn(g, n):
    for i in range(n):
        yield(next(g))

firstn(efg, 2)




