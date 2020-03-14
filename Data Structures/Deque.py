#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 24 14:58:09 2020

@author: natnem
"""

class Deque(object):
    """in this implementation adding and removing items from the front
        is O(1) whereas adding and removing from the rear is O(n)"""
    def __init__(self):
        self.deque = []
    
    def isEmpty(self):
        if self.deque == []:
            return True
        else: return False
    def size(self):
        return len(self.deque)
    def addFront(self, item):
        self.deque.append(item)
    def addRear(self, item):
        self.deque.insert(0 , item)
    def removeFront(self):
        if self.isEmpty():
            raise Exception("Deque Empty")
        else:
            front = self.deque.pop()
            return front
    def removeRear(self):
        if self.isEmpty():
            raise Exception("Deque Empty")
        else:
            rear = self.deque.pop(0)
            return rear
    def deq(self):
        return self.deque

#d = Deque()
#print(d.isEmpty())
#d.addRear(4)
#d.addRear(5)
#print(d.deq())
#d.addFront("front")
#print(d.deq())
    





#PALINDROME CHECKER USING THE DEQUE
def isPal(mystring):
    myDeq = Deque()
    for char in range(len(mystring)):
        myDeq.addRear(mystring[char])
 
    equal = True
    while myDeq.size() > 1 and equal :
        front = myDeq.removeFront()
        last = myDeq.removeRear()
        if front != last:
            equal = False
    return equal
    
mystr = "madam"
print(isPal(mystr))
        