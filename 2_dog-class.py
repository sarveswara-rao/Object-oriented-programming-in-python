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
        
    # method for doginfo
    def doginfo(self):
        print(f"{self.name} is {self.age} year(s) old.")
    
    # birthday method adds one year to dog's age
    def birthday(self):
        print(f'\nHappy Birthday {self.name}.', end=' Now, ')
        self.age += 1
        # now call the doginfo to see the changes
        self.doginfo()
        
    def setBuddy(self, buddy):
        self.buddy = buddy
        buddy.buddy = self
    
# instantiating the class to create a oz object
ch = Dog("chinnu", 2)
tom = Dog('Tommy', 3)
mc = Dog('Michael', 4)

# calling the each object's info method using dot
ch.doginfo()
tom.doginfo()
mc.doginfo()

# Omg, today is chinnu birthday
ch.birthday()

tom.birthday()

# set chinny buddy as tommy
ch.setBuddy(tom)
# print chinnu buddy age and name
print('\n', ch.buddy.age, ch.buddy.name)
print('\n', tom.buddy.age, tom.buddy.name)

ch.buddy.doginfo()