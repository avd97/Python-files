# -*- coding: utf-8 -*-
"""
Created on Thu Feb 14 11:23:28 2019

@author: VVD
"""

#  Labda function: small Anonymous function

x = lambda a: a*10
print(x(5))

y = lambda a,b,c: a+b+c
print(y(5,4,6))


def func(n):
    return lambda a:a*n    #returns the pointer of function
                            #returns othe address of anonymous function

x = func(4)
print(x)

mydouble = func(44)  
print(mydouble(44))