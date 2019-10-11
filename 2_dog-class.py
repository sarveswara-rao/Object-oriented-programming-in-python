# -*- coding: utf-8 -*-
"""
Created on Fri Oct 11 06:58:46 2019

@author: sarveswara rao
"""

# to create a class, we have to use the class keyword
class Dog:
   
    # constructer for the class
    def __init__(self, name, age):
        self.name = name
        self.age = age
    # adding a new method (aka its function)
    def bark(self):
        print('who is that!!, bow! bow! bow!!!!')
        
# instantiating the class to create a oz object
oz = Dog("chunnu", 2)
print(oz)
print(f"\n{oz.name} is {oz.age} year(s) old.")
oz.bark()
