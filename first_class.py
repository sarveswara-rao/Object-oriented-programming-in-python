# -*- coding: utf-8 -*-
"""
Created on Fri Oct 11 06:49:14 2019

@author: sarveswara rao
"""

# to create a class, we have to use the class keyword
class Dog:
   
    # constructer for the class
    def __init__(self, name, age):
        self.name = name
        self.age = age

# instantiating the class to create a oz object
oz = Dog("chunnu", 6)
print(oz)
print(f"{oz.name} is {oz.age} year(s) old.")