#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 27 09:54:20 2020

@author: natnem
"""

class Node(object):
    def __init__(self, item):
        self.data = item
        self.next = None
    def getData(self):
        return self.data
    def getNext(self):
        return self.next
    def setNext(self, newNext):
        self.next  = newNext
    def setData(self, newData):
        self.data = newData
    

class OrderedList(Node):
    def __init__(self):
        self.head = None
    def size(self):
        """Returns the size of the list"""
        count = 0
        cur = self.head
        while(cur != None):
            cur = cur.next
            count += 1
        return count
    def isEmpty(self):
        return self.size() == 0
    def display(self):
        """Displays the list"""
        cur = self.head
        n = []
        for ind in range(self.size()):
            n.append(cur.data)
            cur = cur.next
        return n
            
    def add(self, item):
        """adds a new item to the list making sure that the order is preserved"""
        current = self.head
        prev = None
        stop = False
        while current != None and not stop:
                if current.data > item:
                    stop = True
                else:
                    prev = current
                    current = current.next
        temp = Node(item)
        if prev == None:
            temp.setNext(current)
            self.head = temp
        else:
            temp.setNext(current)
            prev.setNext(temp)
    
    def search(self , item):
        """Searches for an item in the list and returns the index"""
        count = 0
        current = self.head
#        print(self.size(), self.display())
        while current != None:
            if current.getData() == item:
                return count
            else:
                count += 1
                current = current.next
        
        raise Exception("Item Not Found")
    
                
    def pop(self, pos):
        """returns the item at index pos(must be positive), and deletes it from the list"""
        prev = None
        current = self.head
        counter = 0
        Found  = False
        if pos < 0 or pos > self.size():
            raise Exception("Index out of range")
        while current != None and not Found:
            if counter == pos:
                Found = True
            else:
                prev = current
                current = current.next
                counter += 1
        temp = current.getData()
        if prev == None:
            self.head = current.next     
        else:
            prev.setNext(current.next)
        return temp
            
            
        
        
            
        
            
        
myorderedList = OrderedList()
print(myorderedList.display())
myorderedList.add(1)
myorderedList.add(10)
#myorderedList.add(2)
myorderedList.add(3)
myorderedList.add(10)
myorderedList.add(2)
print(myorderedList.display())
#print(myorderedList.search(10))
print(myorderedList.pop(2))
print(myorderedList.display())
