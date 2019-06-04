# -*- coding: utf-8 -*-
"""
Created on Thu Feb 14 11:23:28 2019

@author: VVD
"""

#  Self: reference to the class instance itself
# used to access vaiables that belongs to the class
 #Everythin in python is private

# Abstract class:used as base class to create new class 
 
class Shape2D:
     def area(self):
         raise NotImplementedError()
         
class Shape3D:
    def volume(self):
        raise NotImplementedError()
        
class square(Shape2D):
    def __init__(self,width):
        self, width = width
        
    def area(self):
        return self.width ** 2
 
ob1 = square()
#ob2 = Shape3D()

ob1.area(4)
