#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 24 11:26:39 2020

@author: natnem
"""

class Queue_Two(object):
    """Uses a List, Enqueue is at the rear which is always at index 0
        it uses the insert method of List which takes O(n)
        and Dequeue is at the end which is appending and 
        it takes constant time """
    def __init__(self):
        self.queue = []
    def isEmpty(self):
        return self.queue == []
    def size(self):
        return len(self.queue)
    def Enqueue(self,item):
        self.queue.insert(0,item)
    def Dequeue(self):
        if not self.isEmpty():
            return self.queue.pop()
        else:
            raise Exception("Queue is Empty")
    def peek(self):
        return self.queue[self.size()-1]
    def print(self):
        return self.queue
    
        
#q = Queue_Two()   
#q.Enqueue("dog")
#q.Enqueue("cat")
#print(q.print())
#q.Dequeue()
#print(q.print())



#import random        
#def HotPotatoGame(NameList):
#    Q = Queue_Two()
#    for i in range(len(NameList)):
#        Q.Enqueue(NameList[i])
#    print(Q.print())
#    print()
#    while Q.size() > 1 :
#        num = random.randint(0,10)
#        for i in range(num):
#            Q.Enqueue(Q.Dequeue())
#            print(Q.print(),num)
#        Q.Dequeue()
#        
#    return Q.peek()
#Name = ["Bill","David","Susan","Jane","Kent","Brad"]
#print(HotPotatoGame(Name))
        
    