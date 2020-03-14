#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 22 09:35:33 2020

@author: natnem
"""

class Queue(object):
    def __init__(self, queueSize):
        self.queuesize = queueSize
        self.queue = [0]*queueSize
        self.size = 0
        self.rear = 0
        self.front = 0
    def myqueue(self): return self.queue
    def isEmpty(self):
        return self.size == 0
    def isFull(self):
        return self.size == self.queuesize 
    def FrontIndex(self): return self.front
    def RearIndex(self): return self.rear
    def Enqueue(self, item):
        if self.isFull():
            raise Exception("Queue is Full")
        else:
            
            self.queue[self.RearIndex()] = item
            self.size += 1
            self.rear = (self.rear + 1) % self.queuesize
    def Dequeue(self):
        if self.isEmpty():
            raise Exception("Queue is Empty")
        else:
            value = self.queue[self.FrontIndex()]
            self.size  -= 1
            self.queue[self.FrontIndex()] = 0 
            self.front = (self.front + 1) % self.queuesize
            
            return value


myque = Queue(10)
print(myque.myqueue())
myque.Enqueue(1)
myque.Enqueue(2)
myque.Enqueue(5)
myque.Enqueue(10)
myque.Enqueue(7)
myque.Enqueue(18)
print(myque.myqueue())
myque.Dequeue()
myque.Dequeue()
myque.Enqueue(1)
myque.Enqueue(10)
myque.Enqueue(7)
myque.Enqueue(18)
print(myque.myqueue())
myque.Enqueue(25)
print(myque.FrontIndex(), myque.RearIndex())
myque.Enqueue(30)
print(myque.myqueue())
#myque.Enqueue(40)
print(myque.myqueue())
print(myque.front, myque.rear)