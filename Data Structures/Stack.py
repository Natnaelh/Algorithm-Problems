#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 14 10:26:32 2020

@author: natnem
"""

class Stack(object):
    def __init__(self, stacksize):
        self.stacksize = stacksize
        self.array = [0]*stacksize
        self.size = 0
        
    def isFull(self):
        return self.size == self.stacksize
    def isEmpty(self):
        return self.size == 0
    def TopIndex(self):
        return self.size - 1
    def Push(self, item):
        if self.isFull():
            raise Exception("Stack is Full")
        else:
            self.size += 1
            self.array[self.TopIndex()] = item
    
    def Pop(self):
        if self.isEmpty():
            raise Exception('Stack is Empty')
        else:
            top = self.array[self.TopIndex()]
            self.array[self.TopIndex()] = 0
            self.size -= 1
            return top
    def Peek(self):
        if self.isEmpty():
            raise Exception("Stack is Empty")
        else:
            return self.array[self.TopIndex()]

        
        

mystack = Stack(10)
print(mystack.array)
mystack.Push(5)
mystack.Push(10)
mystack.Push(15)
print(mystack.array)
print(mystack.Pop())
print(mystack.array)
        