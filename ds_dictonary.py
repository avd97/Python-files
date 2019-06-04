# -*- coding: utf-8 -*-
"""
Created on Thu Feb 14 11:23:28 2019

@author: VVD
"""

#   Data Strucrtures:
#   4.. dictonary-   unoredered & changabl & indexed collection in key:values pair    

thisdict = {"Brand":"Land Rover","Price":45000000,"Model":"VELAR"}
print(thisdict)

#print("Brand")

#for x in thisdict:
    #print(type(x))
 #   print(x)
    
for x,y in thisdict.items():
    print(x,": ",y)
    
if "Brand" in thisdict:
    print("Key Available.")
else:
    print("Not Available !")
    
    
print(len(thisdict))

thisdict.pop("Brand")   #   Removes key enetered element
print(thisdict)

thisdict.popitem()  #removes last itemfrom dictionary
print(thisdict)


##using dict() constructor
