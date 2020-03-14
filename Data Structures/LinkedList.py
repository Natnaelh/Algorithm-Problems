#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 22 11:22:32 2020

@author: natnem
"""

class Node(object):
    """ Unsorted linked list """
    def __init__(self , intialData): ##creates a new ordered list that is empty
        self.data  = intialData
        self.next = None
    def getData(self):
        return self.data
    def getNext(self):
        return self.next
    def setData(self, newData):
        self.data = newData
    def setNext(self, newNext):
        self.next = newNext

#node = Node(93)
#print(node.data)
#print(node.next)
#x = node.setNext(50)
#print(node.next)

class LinkedList(Node):  
    def __init__(self):
        self.head = None
    
    def isEmpty(self):
        return self.head == None
    def add(self , item): #adds item to the head
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp
    def size(self):
        current  = self.head
        counter = 0
        while current != None:
            current = current.next
            counter += 1
        return counter
    
    def display(self):
        n = []
        m = self.head
        for i in range(self.size()):
            n.append(m.data)
            m = m.next
        return n
    
    def search(self,key):
        current = self.head
        while current != None:
            if current.data == key:
                return current
            current = current.getNext()
        return current
    def remove(self,item):
        current = self.head
        prev = None
        found = False
        if self.isEmpty():
            raise Exception("List Empty")
        while not found:
            if current.getData() == item:
                found = True
            else:
                prev = current
                current = current.getNext()
        if prev == None:
            self.head = current.getNext()
        else:
            prev.setNext(current.getNext())
    
    def index(self, item):  #returns the position of item in the list
        ind = 0
        cur = self.head
        while cur != None:
            if cur.data == item:
                return ind
            else:
                cur = cur.next
                ind  += 1
                
    def append(self , item): #adds a new item to the end of the list making it the last item
        s = self.size()
        curr = self.head
        temp = Node(item)
        for i in range(s-1):
            curr = curr.next
        curr.setNext(temp)
        return self
        
#adds a new item to the list at position pos,  if pos is larger than the 
# size of the list , then it will just append it at the end
    def insert(self,pos,item): 
        temp = Node(item)
        if pos < 0:
            raise Exception("Invalid Index for item")
        if pos  == 0:
            self.add(item)
        elif pos >= self.size():
            self.append(item)
        else:
            cur = self.head
            count = 0
            while cur != None:
                if count == pos - 1:
                    break
                else:
                    cur = cur.next
                    count += 1
            temp.setNext(cur.next)
            cur.setNext(temp)
        return self.display()
    
        
                

          
           
           
       
            
                
    
                
#mylist = LinkedList()
#mylist.add(5)
#mylist.add(10)
#mylist.add(1)
#mylist.add(0)
#print(mylist.size())
#print(mylist.display())
#print(mylist.append(2))
#print(mylist.insert(10,20))

        
        
        
        
    
    